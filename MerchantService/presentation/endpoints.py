from typing import Union

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status

from business.merchant_service import MerchantService
from infrastructure.container import Container
from models.empty_model import EmptyModel
from models.merchant import Merchant

router = APIRouter(prefix='/merchants')


@router.get('/{merchant_id}', status_code=status.HTTP_200_OK)
@inject
async def get_merchant(merchant_id: str,
                       merchant_service: MerchantService = Depends(Provide[Container.merchant_service])):
    merchant: Union[Merchant, EmptyModel] = merchant_service.get_merchant(int(merchant_id))
    if isinstance(merchant, EmptyModel):
        raise HTTPException(404, 'Merchant does not exist.')
    return merchant


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def post_merchant(merchant: Merchant,
                        merchant_service: MerchantService = Depends(Provide[Container.merchant_service])):
    inserted_merchant_id: int = merchant_service.post_merchant(merchant)
    return {'message': f'Inserted merchant with ID {inserted_merchant_id}'}
