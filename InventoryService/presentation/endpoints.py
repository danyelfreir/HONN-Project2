from typing import Union

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from business.product_service import ProductService
from infrastructure.container import Container
from models.empty_model import EmptyModel
from models.product_model import ProductModel

router = APIRouter(prefix='/products')


@router.get('/{product_id}', status_code=status.HTTP_200_OK)
@inject
async def get_products(product_id: str, product_service: ProductService = Depends(Provide[Container.product_service])):
    product: Union[ProductModel, EmptyModel] = product_service.get_product(int(product_id))
    if isinstance(product, EmptyModel):
        raise HTTPException(404, 'Product does not exist')
    return product


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def post_product(product: ProductModel,
                       product_service: ProductService = Depends(Provide[Container.product_service])):
    inserted_product_id: int = product_service.post_product(product)
    return {'message': f'Inserted product with ID {inserted_product_id}'}


@router.post('/{product_id}', status_code=status.HTTP_200_OK)
@inject
async def reserve_product(product_id: int, product_service: ProductService = Depends(Provide[Container.product_service])):
    total_reserved_products = product_service.reserve_product(product_id)
    if total_reserved_products < 0:
        raise HTTPException(404, 'No products to reserve')
    return {
        'message': 'Reserved',
        'product_id': product_id,
        'total_reserved': total_reserved_products
    }
