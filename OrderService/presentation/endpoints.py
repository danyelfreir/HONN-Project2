
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status
import requests
from typing import Union

from business.order_service import OrderService
from infrastructure.container import Container
from models.empty_model import EmptyModel
from models.order import Order, SavedOrder, ForwardOrder
from presentation.exchange import Exchange

router = APIRouter(prefix='/orders')

exchange = Exchange()


@router.get('/{order_id}', status_code=status.HTTP_200_OK)
@inject
async def get_order(order_id: int, order_service: OrderService = Depends(Provide[Container.order_service])):
	order: Union[SavedOrder, EmptyModel] = order_service.get_order(order_id)
	if isinstance(order, EmptyModel):
		raise HTTPException(404, 'Order does not exist.')
	return order

@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def post_order(order: Order, order_service: OrderService = Depends(Provide[Container.order_service])):
	order = order.dict()
	# if merchant does not exist
	merchant = get_merchant(order['merchant_id'])
	if merchant.status_code == 404:
		raise HTTPException(404, 'Merchant does not exist.')
	merchant = merchant.json()
	
	# if buyer does not exist
	buyer = get_buyer(order['buyer_id'])
	if buyer.status_code == 404:
		raise HTTPException(404, 'Buyer does not exist.')
	buyer = buyer.json()

	# if product does not exist
	inventory = get_inventory(order['product_id'])
	if inventory.status_code == 404:
		raise HTTPException(404, 'Product does not exist.')
	inventory = inventory.json()

	# if product does exist but is sold out
	if ( inventory['quantity'] == 0 ) or ( inventory['quantity'] - inventory['reserved'] == 0 ):
		raise HTTPException(404, 'Product is sold out.')

	# if product is not sold by merchant
	if order['merchant_id'] != inventory['merchant_id']:
		raise HTTPException(404, 'Product does not belong to merchant.')

	# if merchant does not allow discounts and discount field is other than 0 or null
	if (order['discount'] != 0 or order['discount'] is None) and merchant['allows_discount'] is False:
		raise HTTPException(404, 'Merchant does not allow discount.')

	order_to_save = SavedOrder(
		        product_id=order['product_id'],
                merchant_id=order['merchant_id'],
                buyer_id=order['buyer_id'],
                card_number=order['credit_card']['card_number'],
                total_price=(1 - order['discount']) * inventory['price']
	)

	# save with credit card info hidden with ****
	inserted_order_id: int  = order_service.post_buyer(order_to_save)

	order_to_forward = ForwardOrder(
		order_id = inserted_order_id,
		product_id = order['product_id'],
		merchant_id = order['merchant_id'],
		buyer_id = order['buyer_id'],
		buyer = buyer,
		credit_card = order['credit_card'],
		total_price=(1 - order['discount']) * inventory['price'],
		inventory = inventory
		)

	# reserve product
	post_reserve_inventory(order['product_id'])
	# publish order
	exchange.publish(order_to_forward.json())
	return {'message': f'Inserted order with ID {inserted_order_id}'}


def get_merchant(merchant_id: int):
	return requests.get(f'http://merchant_service:8001/merchants/{merchant_id}')

def get_buyer(buyer_id: int):
	return requests.get(f'http://buyer_service:8002/buyers/{buyer_id}')

def get_inventory(product_id: int):
	return requests.get(f'http://inventory_service:8003/products/{product_id}')


def post_reserve_inventory(product_id: int):
	return requests.post(f'http://inventory_service:8003/products/{product_id}')