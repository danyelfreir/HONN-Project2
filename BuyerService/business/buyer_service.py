from typing import Union

from models.empty_model import EmptyModel
from models.buyer_model import BuyerModel
from models.buyer_dto import BuyerDTO
from persistence.buyer_repository import BuyerRepository


class BuyerService:
    def __init__(self, repository: BuyerRepository):
        self.__repository = repository

    def get_buyer(self, buyer_id: int) -> Union[BuyerModel, EmptyModel]:
        return self.__repository.get_buyer(buyer_id)

    def post_buyer(self, buyer: BuyerDTO) -> int:
        return self.__repository.create_buyer(buyer)
