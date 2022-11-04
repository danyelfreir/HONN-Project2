from typing import Union

from models.empty_model import EmptyModel
from models.product_model import ProductModel
from persistence.postgres_connection import PostgresConnection


class ProductRepository:
    def __init__(self, database_connection: PostgresConnection) -> None:
        self.__database_connection = database_connection

    def create_product(self, product: ProductModel):
        product_dict: dict = product.dict()
        command = """INSERT INTO product(merchantId, productName, price, quantity, reserved)
                     VALUES (%(merchantId)s, %(productName)s, %(price)s, %(quantity)s, %(reserved)s)
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
            return ProductModel(
                merchantId=product_from_db[1],
                productName=product_from_db[2],
                price=product_from_db[3],
                quantity=product_from_db[4],
                reserved=product_from_db[5],
            )
        return EmptyModel()
