from typing import Union

from fastapi import APIRouter, HTTPException, status
import requests

# order:    8000
# merchant: 8001
# buyer:    8002
# products: 8003

router = APIRouter(prefix='/api')


# ORDER ENDPOINTS
@router.get('/orders/{order_id}', status_code=status.HTTP_201_CREATED)
async def get_order(order_id: int):
    response = requests.get(f'http://order_service:8000/orders/{order_id}')
    response_json = response.json()
    if response.status_code == 404:
        raise HTTPException(404, response_json['detail'])
    return response_json


@router.post('/orders', status_code=status.HTTP_201_CREATED)
async def post_order(order: dict):
    return requests.post(f'http://order_service:8000/orders/', json=order).json()


# MERCHANT ENDPOINTS
@router.get('/merchants/{merchant_id}', status_code=status.HTTP_200_OK)
async def get_merchant(merchant_id: int):
    response = requests.get(f'http://merchant_service:8001/merchants/{merchant_id}')
    response_json = response.json()
    if response.status_code == 404:
        raise HTTPException(404, response_json['detail'])
    return response_json


@router.post('/merchants', status_code=status.HTTP_201_CREATED)
async def post_merchant(merchant: dict) -> int:
    return requests.post(f'http://merchant_service:8001/merchants/', json=merchant).json()


# BUYER ENDPOINTS
@router.get('/buyers/{buyer_id}', status_code=status.HTTP_200_OK)
async def get_buyer(buyer_id: int) -> Union[dict, None]:
    response = requests.get(f'http://buyer_service:8002/buyers/{buyer_id}')
    response_json = response.json()
    if response.status_code == 404:
        raise HTTPException(404, response_json['detail'])
    return response_json


@router.post('/buyers/', status_code=status.HTTP_201_CREATED)
async def post_buyer(buyer: dict) -> int:
    return requests.post('http://buyer_service:8002/buyers/', json=buyer).json()


# PRODUCT ENDPOINTS
@router.get('/products/{product_id}', status_code=status.HTTP_200_OK)
async def get_products(product_id: int) -> Union[dict, None]:
    response = requests.get(
        f'http://inventory_service:8003/products/{product_id}')
    response_json = response.json()
    if response.status_code == 404:
        raise HTTPException(404, response_json['detail'])
    return response_json


@router.post('/products/', status_code=status.HTTP_201_CREATED)
async def post_product(product: dict) -> int:
    return requests.post('http://inventory_service:8003/products/', json=product).json()



