from typing import Union

from models.empty_model import EmptyModel
from models.order import Order
from persistence.order_repository import OrderRepository


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.__repository = repository

    def get_order(self, order_id: int) -> Union[Order, EmptyModel]:
        return self.__repository.get_order(order_id)

    def post_buyer(self, order: Order) -> int:
        return self.__repository.create_order(order)
