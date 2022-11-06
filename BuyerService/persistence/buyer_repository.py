from typing import Union

from models.empty_model import EmptyModel
from models.buyer_model import BuyerModel
from models.buyer_dto import BuyerDTO
from persistence.postgres_connection import PostgresConnection


class BuyerRepository:
    def __init__(self, database_connection: PostgresConnection) -> None:
        self.__database_connection = database_connection

    def create_buyer(self, buyer: BuyerDTO):
        buyer_dict: dict = buyer.dict()
        command = """INSERT INTO buyer(name, ssn, email, phone_number)
                     VALUES (%(name)s, %(ssn)s, %(email)s, %(phone_number)s)
                     RETURNING buyer_id;"""
        inserted_buyer_id: int = self.__database_connection.insert(command, buyer_dict)
        self.__database_connection.commit()
        return inserted_buyer_id

    def get_buyer(self, buyer_id: int) -> Union[BuyerModel, EmptyModel]:
        id_dict = {'buyer_id': buyer_id}
        command = """SELECT * FROM buyer
                     WHERE buyer_id = %(buyer_id)s;"""
        buyer_from_db = self.__database_connection.fetch(command, id_dict)
        if buyer_from_db is not None:
            return BuyerModel(**buyer_from_db)
        return EmptyModel()
