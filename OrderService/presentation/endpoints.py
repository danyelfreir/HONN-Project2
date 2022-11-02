
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status
import requests

from business.order_service import OrderService
from infrastructure.container import Container
from models.empty_model import EmptyModel
from models.order import Order
from exchange import Exchange

router = APIRouter(prefix='/orders')

exchange = Exchange()


@router.get('/{order_id}', status_code=status.HTTP_200_OK)
@inject
async def get_order(order_id: int, order_service: OrderService = Depends(Provide[Container.order_service])):
	order: Union[Order, EmptyModel] = order_service.get_order(order_id)
	if isinstance(order, EmptyModel):
		raise HTTPException(404, 'Order does not exist.')
	# TODO: change discount to price before returning
	return order

@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def post_order(order: Order, order_service: OrderService = Depends(Provide[Container.order_service])):
	# TODO: if merchant does not exist
	merchant = get_merchant(order['merchant_id'])
	if merchant is None:
		raise HTTPException(404, 'Merchant does not exist.')
	# TODO: if buyer does not exist
	buyer = get_buyer(order['buyer_id'])
	if buyer is None:
		raise HTTPException(404, 'Buyer does not exist.')
	# TODO: if product does not exist
	inventory = get_inventory(order['product_id'])
	if inventory is None:
		raise HTTPException(404, 'Product does not exist.')
	# TODO: if product does exist but is sold out
	elif ( inventory['quantity'] == 0 ) or ( inventory['quantity'] - inventory['reserved'] == 0 ):
		raise HTTPException(404, 'Product is sold out.')
	# TODO: if product is not sold by merchant
	if merchant['merchant_id'] != inventory['merchant_id']:
		raise HTTPException(404, 'Product does not belong to merchant.')
	# TODO: if merchant does not allow discounts and discount field is other than 0 or null
	if order['discount'] != 0 and merchant['allowsDiscount'] is False:
		raise HTTPException(404, 'Merchant does not allow discount.')

	# TODO: save with credit card info hidden with ****
	inserted_order_id: int  = order_service.post_buyer(order)
	# publish order
	exchange.publish(order)
	return {'message': f'Inserted order with ID {inserted_order_id}'}


async def get_merchant(merchant_id: int):
	return requests.get('localhost:8000/merchant/%s', merchant_id)


async def get_buyer(buyer_id: int):
	return requests.get('localhost:8000/buyer/%s', buyer_id)

async def get_inventory(product_id: int):
	return requests.get('localhost:8000/products/%s', product_id)


