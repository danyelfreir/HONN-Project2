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
    return requests.get(f'http://inventory_service:8003/products/{product_id}').json()


@router.post('/products', status_code=status.HTTP_201_CREATED)
async def post_product(product: dict) -> int:
    if "reserved" not in product:
        product["reserved"] = 0
    return requests.post(f'http://inventory_service:8003/products/',json=product).json()

@router.post('/products/{product_id}', status_code=status.HTTP_201_CREATED)
async def post_product(product_id: int) -> int:
    return requests.post(f'http://inventory_service:8003/products/{product_id}').json()

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
    return requests.get(f'http://order_service:8000/orders/{order_id}', json=order_id).json()

@router.post('/orders', status_code=status.HTTP_201_CREATED)
async def post_order(order: dict):
    return requests.post(f'http://order_service:8000/orders/', json=order).json()