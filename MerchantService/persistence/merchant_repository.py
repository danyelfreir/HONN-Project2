from typing import Union

from models.empty_model import EmptyModel
from models.merchant import Merchant
from persistence.postgres_connection import PostgresConnection


class MerchantRepository:
    def __init__(self, database_connection: PostgresConnection) -> None:
        self.__database_connection = database_connection

    def create_merchant(self, merchant: Merchant):
        merchant_dict: dict = merchant.dict()
        command = """INSERT INTO merchant(name, ssn, email, phone_number, allows_discount)
                     VALUES (%(name)s, %(ssn)s, %(email)s, %(phoneNumber)s, %(allowsDiscount)s)
                     RETURNING merchant_id;"""
        inserted_merchant_id: int = self.__database_connection.insert(command, merchant_dict)
        self.__database_connection.commit()
        return inserted_merchant_id

    def get_merchant(self, merchant_id: int) -> Union[Merchant, EmptyModel]:
        id_dict = {'merchant_id': merchant_id}
        command = """SELECT * FROM merchant
                     WHERE merchant_id = %(merchant_id)s;"""
        merchant_from_db = self.__database_connection.fetch(command, id_dict)
        if merchant_from_db is not None:
            return Merchant(
                name=merchant_from_db[0],
                ssn=merchant_from_db[1],
                email=merchant_from_db[2],
                phoneNumber=merchant_from_db[3],
                allowsDiscount=merchant_from_db[4]
            )
        return EmptyModel()
