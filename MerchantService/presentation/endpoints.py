from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide
from business.merchant_service import MerchantService
from models.merchant import Merchant
from infrastructure.container import Container

router = APIRouter(prefix='/merchants')

@router.get('/{merchant_id}', status_code=status.HTTP_200_OK)
@inject
async def get_merchant(merchant_id: str, merchant_service: MerchantService = Depends(Provide[Container.merchant_service])):
	merchant: Merchant = merchant_service.get_merchant(int(merchant_id))
	return merchant.dict()

@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def post_merchant(merchant: Merchant, merchant_service: MerchantService = Depends(Provide[Container.merchant_service])):
	merchant_service.post_merchant(merchant)
