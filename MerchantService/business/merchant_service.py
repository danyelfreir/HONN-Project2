from persistence.merchant_repository import MerchantRepository
from models.merchant import Merchant

class MerchantService:
    def __init__(self, repository: MerchantRepository):
        self.__repository = repository

    def get_merchant(self, merchant_id: int) -> Merchant:
        return self.__repository.get_merchant(merchant_id)

    def post_merchant(self, merchant: Merchant) -> None:
        self.__repository.create_merchant(merchant)