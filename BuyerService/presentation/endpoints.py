from typing import Union

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status

from business.buyer_service import BuyerService
from infrastructure.container import Container
from models.empty_model import EmptyModel
from models.buyer import Buyer

router = APIRouter(prefix='/buyers')


@router.get('/{buyer_id}', status_code=status.HTTP_200_OK)
@inject
async def get_buyer(buyer_id: str,
                       buyer_service: BuyerService = Depends(Provide[Container.buyer_service])):
    buyer: Union[Buyer, EmptyModel] = buyer_service.get_buyer(int(buyer_id))
    if isinstance(buyer, EmptyModel):
        raise HTTPException(404, 'Buyer does not exist.')
    return buyer


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def post_buyer(buyer: Buyer,
                        buyer_service: BuyerService = Depends(Provide[Container.buyer_service])):
    print('buyer')
    inserted_buyer_id: int = buyer_service.post_buyer(buyer)
    return {'message': f'Inserted buyer with ID {inserted_buyer_id}'}
