from typing import Union

from models.empty_model import EmptyModel
from models.order import Order, SavedOrder
from persistence.postgres_connection import PostgresConnection


class OrderRepository:
    def __init__(self, database_connection: PostgresConnection) -> None:
        self.__database_connection = database_connection

    def create_order(self, order: Order):
        order_dict: dict = order.dict()
        print(order_dict['card_number'])
        # hide card number
        hidden_number = self.__hide_card_number(order_dict['card_number'])
        order_dict['card_number'] = hidden_number
        # sql command
        command = """INSERT INTO orders(product_id, merchant_id, buyer_id, card_number, total_price)
                     VALUES (%(product_id)s, %(merchant_id)s, %(buyer_id)s, %(card_number)s, %(total_price)s)
                     RETURNING order_id;"""
        # insert into db
        inserted_order_id: int = self.__database_connection.insert(command, order_dict)
        # commit to db
        self.__database_connection.commit()
        # return order_id
        return inserted_order_id

    def get_order(self, order_id: int) -> Union[Order, EmptyModel]:
        id_dict = {'order_id': order_id}
        command = """SELECT * FROM orders
                     WHERE order_id = %(order_id)s;"""
        order_from_db = self.__database_connection.fetch(command, id_dict)
        if order_from_db is not None:
            return SavedOrder(
                product_id=order_from_db[1],
                merchant_id=order_from_db[2],
                buyer_id=order_from_db[3],
                card_number=order_from_db[4],
                total_price=order_from_db[5] 
            )
        return EmptyModel()

    def __hide_card_number(self, card_number: str):
        str_len = len(card_number)
        stars = '*' * (str_len - 4)
        return stars + card_number[str_len-4:]
