from typing import Union

from models.empty_model import EmptyModel
from models.merchant_dto import MerchantDTO
from models.merchant_model import MerchantModel
from persistence.postgres_connection import PostgresConnection


class MerchantRepository:
    def __init__(self, database_connection: PostgresConnection) -> None:
        self.__database_connection = database_connection

    def create_merchant(self, merchant: MerchantDTO):
        command = """INSERT INTO merchant(name, ssn, email, phone_number, allows_discount)
                     VALUES (%(name)s, %(ssn)s, %(email)s, %(phone_number)s, %(allows_discount)s)
                     RETURNING merchant_id;"""
        inserted_merchant_id: int = self.__database_connection.insert(command, merchant.dict())
        self.__database_connection.commit()
        return inserted_merchant_id

    def get_merchant(self, merchant_id: int) -> Union[MerchantModel, EmptyModel]:
        command = """SELECT * FROM merchant
                     WHERE merchant_id = %(merchant_id)s;"""
        merchant_from_db = self.__database_connection.fetch(command, {'merchant_id': merchant_id})
        if merchant_from_db is not None:
            return MerchantModel(**merchant_from_db)
        return EmptyModel()
