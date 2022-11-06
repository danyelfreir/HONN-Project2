from typing import Union

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status
import requests

# merchant : 8002
# payment : 8003
# order : 8004
# api : 8005


router = APIRouter(prefix='/api')

# BUYER ENDPOINTS
@router.get('/buyers/{buyer_id}', status_code=status.HTTP_200_OK)
async def get_buyer(buyer_id: int) -> Union[dict, None]:
    return requests.get(f'http://buyer_service:8004/buyers/{buyer_id}').json()


@router.post('/buyers/', status_code=status.HTTP_201_CREATED)
async def post_buyer(buyer: dict) -> int:
    return requests.post('http://buyer_service:8004/buyers/', json=buyer).json()


# PRODUCT ENDPOINTS
@router.get('/products/{product_id}', status_code=status.HTTP_200_OK)
async def get_products(product_id: int) -> Union[dict, None]:
    response = requests.get(f'http://inventory_service:8003/products/{product_id}').json()
    res_dict = {"merchantId": response["merchant_id"], "productName": response["product_name"], "price": response["price"], "quantity": response["quantity"], "reserved": response["reserved"]}
    return res_dict


@router.post('/products/', status_code=status.HTTP_201_CREATED)
async def post_product(product: dict) -> int:
    product["reserved"] = 0
    req_dict = {"merchant_id": product["merchantId"], "product_name": product["productName"], "price": product["price"], "quantity": product["quantity"], "reserved": 0}
    return requests.post('http://inventory_service:8003/products/', json=req_dict).json()


# MERCHANT ENDPOINTS
@router.get('/merchants/{merchant_id}', status_code=status.HTTP_200_OK)
async def get_merchant(merchant_id: int):
    return requests.get(f'http://merchant_service:8002/merchants/{merchant_id}').json()


@router.post('/merchants', status_code=status.HTTP_201_CREATED)
async def post_merchant(merchant: dict) -> int:
    return requests.post(f'http://merchant_service:8002/merchants/', json=merchant).json()


# ORDER ENDPOINTS
@router.get('/orders/{order_id}', status_code=status.HTTP_201_CREATED)
async def get_order(order_id: int):
    response = requests.get(f'http://order_service:8000/orders/{order_id}', json=order_id).json()
    res_dict = {"productId": response["product_id"], "merchantId": response["merchant_id"], "buyerId": response["buyer_id"], "cardNumber": response["card_number"], "totalPrice ": response["total_price"]}
    return res_dict


@router.post('/orders', status_code=status.HTTP_201_CREATED)
async def post_order(order: dict):
    req_dict = {"product_id": order["productId"], "merchant_id": order["merchantId"], "buyer_id": order["buyerId"], "credit_card": {"card_number": order["creditCard"]["cardNumber"], "expiration_month": order["creditCard"]["expirationMonth"], "expiration_year": order["creditCard"]["expirationYear"], "cvc": order["creditCard"]["cvc"]}, "discount": order["discount"]}
    return requests.post(f'http://order_service:8000/orders/', json=req_dict).json()