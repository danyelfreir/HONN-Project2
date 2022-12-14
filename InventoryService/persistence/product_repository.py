from typing import Union

from models.empty_model import EmptyModel
from models.product_model import ProductModel
from persistence.postgres_connection import PostgresConnection


class ProductRepository:
    def __init__(self, database_connection: PostgresConnection) -> None:
        self.__database_connection = database_connection

    def create_product(self, product: ProductModel):
        product_dict: dict = product.dict()
        command = """INSERT INTO product(merchant_id, product_name, price, quantity, reserved)
                     VALUES (%(merchant_id)s, %(product_name)s, %(price)s, %(quantity)s, %(reserved)s)
                     RETURNING product_id;"""
        inserted_product_id: int = self.__database_connection.insert(command, product_dict)
        self.__database_connection.commit()
        return inserted_product_id

    def get_product(self, product_id: int) -> Union[ProductModel, EmptyModel]:
        id_dict = {'product_id': product_id}
        command = """SELECT * FROM product
                     WHERE product_id = %(product_id)s;"""
        product_from_db = self.__database_connection.fetch(command, id_dict)
        if product_from_db is not None:
            return ProductModel(**product_from_db)
        return EmptyModel()

    def reserve_product(self, product_id: int):
        id_dict = {'product_id': product_id}
        command = """UPDATE product
                     SET reserved = reserved + 1
                     WHERE product_id = %(product_id)s
                     RETURNING reserved;"""
        updated_reservations: int = self.__database_connection.update(command, id_dict)
        self.__database_connection.commit()
        return updated_reservations

    def unreserve_product(self, product_id: int) -> int:
        id_dict = {'product_id': product_id}
        command = """UPDATE product
                     SET reserved = reserved - 1
                     WHERE product_id = %(product_id)s
                     RETURNING reserved;"""
        updated_reservations: int = self.__database_connection.update(command, id_dict)
        self.__database_connection.commit()
        return updated_reservations

    def sell_product(self, product_id: int) -> int:
        command = """UPDATE product
                     SET quantity = quantity - 1,
                         reserved = reserved - 1
                     WHERE product_id = %(product_id)s
                     RETURNING quantity"""
        updated_reservations: int = self.__database_connection.update(command, {'product_id': product_id})
        self.__database_connection.commit()
        return updated_reservations
