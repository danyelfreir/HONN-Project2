from typing import Union

from models.empty_model import EmptyModel
from models.buyer import Buyer
from persistence.buyer_repository import BuyerRepository


class BuyerService:
    def __init__(self, repository: BuyerRepository):
        self.__repository = repository

    def get_buyer(self, buyer_id: int) -> Union[Buyer, EmptyModel]:
        return self.__repository.get_buyer(buyer_id)

    def post_buyer(self, buyer: Buyer) -> int:
        return self.__repository.create_buyer(buyer)
