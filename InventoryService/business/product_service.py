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
        return self.__repo.create_product(product)

    def reserve_product(self, product_id: int) -> int:
        total_products_available: Union[ProductModel, EmptyModel] = self.get_product(product_id)
        if isinstance(total_products_available, EmptyModel) or total_products_available.quantity < 1:
            return -1
        return self.__repo.reserve_product(product_id)

    def unreserve_product(self, product_id: int) -> int:
        total_products_available: Union[ProductModel, EmptyModel] = self.get_product(product_id)
        if isinstance(total_products_available, EmptyModel) or total_products_available.quantity < 1:
            return -1
        return self.__repo.unreserve_product(product_id)

    def sell_product(self, product_id) -> int:
        total_products_available: Union[ProductModel, EmptyModel] = self.get_product(product_id)
        if isinstance(total_products_available, EmptyModel) or total_products_available.quantity < 1:
            return -1
        return self.__repo.sell_product(product_id)
