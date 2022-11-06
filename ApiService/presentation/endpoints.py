from typing import Union

from fastapi import APIRouter, HTTPException, status
import requests

# merchant : 8002
# payment : 8003
# order : 8004
# api : 8005


router = APIRouter(prefix='/api')



# BUYER ENDPOINTS
@router.get('/buyers/{buyer_id}', status_code=status.HTTP_200_OK)
async def get_buyer(buyer_id: int) -> Union[dict, None]:
    response = requests.get(f'http://buyer_service:8004/buyers/{buyer_id}')
    response_json = response.json()
    if response.status_code == 404:
        raise HTTPException(404, response_json['detail'])
    res_dict = {
        "buyerId": response_json['buyer_id'],
        "ssn": response_json['ssn'],
        "name": response_json['name'],
        "email": response_json['email'],
        "phoneNumber": response_json['phone_number']
    }
    return res_dict


@router.post('/buyers/', status_code=status.HTTP_201_CREATED)
async def post_buyer(buyer: dict) -> int:
    req_dict = {
        "name": buyer['name'],
        "ssn": buyer['ssn'],
        "email": buyer['email'],
        "phone_number": buyer['phoneNumber']
    }
    return requests.post('http://buyer_service:8004/buyers/', json=req_dict).json()


# PRODUCT ENDPOINTS
@router.get('/products/{product_id}', status_code=status.HTTP_200_OK)
async def get_products(product_id: int) -> Union[dict, None]:
    response = requests.get(
        f'http://inventory_service:8003/products/{product_id}')
    response_json = response.json()
    if response.status_code == 404:
        raise HTTPException(404, response_json['detail'])
    res_dict = {
        "productId": response_json["product_id"],
        "merchantId": response_json["merchant_id"],
        "productName": response_json["product_name"],
        "price": response_json["price"],
        "quantity": response_json["quantity"],
        "reserved": response_json["reserved"]
    }
    return res_dict


@router.post('/products/', status_code=status.HTTP_201_CREATED)
async def post_product(product: dict) -> int:
    req_dict = {
        "merchant_id": product["merchantId"],
        "product_name": product["productName"],
        "price": product["price"],
        "quantity": product["quantity"],
        "reserved": 0
    }
    return requests.post('http://inventory_service:8003/products/', json=req_dict).json()


# MERCHANT ENDPOINTS
@router.get('/merchants/{merchant_id}', status_code=status.HTTP_200_OK)
async def get_merchant(merchant_id: int):
    response = requests.get(
        f'http://merchant_service:8002/merchants/{merchant_id}')
    response_json = response.json()
    if response.status_code == 404:
        raise HTTPException(404, response_json['detail'])
    res_dict = {
        "merchantId": response_json['merchant_id'],
        "name": response_json['name'],
        "ssn": response_json['ssn'],
        "email": response_json['email'],
        "phoneNumber": response_json['phone_number'],
        "allowsDiscount": response_json['allows_discount']
    }
    return res_dict


@router.post('/merchants', status_code=status.HTTP_201_CREATED)
async def post_merchant(merchant: dict) -> int:
    req_dict = {
        "name": merchant['name'],
        "ssn": merchant['ssn'],
        "email": merchant['email'],
        "phone_number": merchant['phoneNumber'],
        "allows_discount": merchant['allowsDiscount']
    }
    return requests.post(f'http://merchant_service:8002/merchants/', json=req_dict).json()


# ORDER ENDPOINTS
@router.get('/orders/{order_id}', status_code=status.HTTP_201_CREATED)
async def get_order(order_id: int):
    response = requests.get(f'http://order_service:8000/orders/{order_id}')
    response_json = response.json()
    if response.status_code == 404:
        raise HTTPException(404, response_json['detail'])
    res_dict = {
        "productId": response_json["product_id"],
        "merchantId": response_json["merchant_id"],
        "buyerId": response_json["buyer_id"],
        "cardNumber": response_json["card_number"],
        "totalPrice ": response_json["total_price"]
    }
    return res_dict


@router.post('/orders', status_code=status.HTTP_201_CREATED)
async def post_order(order: dict):
    req_dict = {
        "product_id": order["productId"],
        "merchant_id": order["merchantId"],
        "buyer_id": order["buyerId"],
        "credit_card": {
            "card_number": order["creditCard"]["cardNumber"],
            "expiration_month": order["creditCard"]["expirationMonth"],
            "expiration_year": order["creditCard"]["expirationYear"],
            "cvc": order["creditCard"]["cvc"]
        },
        "discount": order["discount"]
    }
    return requests.post(f'http://order_service:8000/orders/', json=req_dict).json()
