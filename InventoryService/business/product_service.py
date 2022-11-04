from typing import Union

from models.empty_model import EmptyModel
from models.product_model import ProductModel
from persistence.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.__repo = repository

    def get_product(self, product_id: int) -> Union[ProductModel, EmptyModel]:
        return self.__repo.get_product(product_id)

    def post_product(self, product: ProductModel) -> int:
        print(product)
        return self.__repo.create_product(product)
