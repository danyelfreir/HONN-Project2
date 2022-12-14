from typing import Union

from models.empty_model import EmptyModel
from models.merchant_dto import MerchantDTO
from models.merchant_model import MerchantModel
from persistence.merchant_repository import MerchantRepository


class MerchantService:
    def __init__(self, repository: MerchantRepository):
        self.__repository = repository

    def get_merchant(self, merchant_id: int) -> Union[MerchantModel, EmptyModel]:
        return self.__repository.get_merchant(merchant_id)

    def post_merchant(self, merchant: MerchantDTO) -> int:
        return self.__repository.create_merchant(merchant)
