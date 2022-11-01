from typing import Union

from models.empty_model import EmptyModel
from models.buyer import Buyer
from persistence.postgres_connection import PostgresConnection


class BuyerRepository:
    def __init__(self, database_connection: PostgresConnection) -> None:
        self.__database_connection = database_connection

    def create_buyer(self, buyer: Buyer):
        buyer_dict: dict = buyer.dict()
        command = """INSERT INTO buyer(name, ssn, email, phone_number)
                     VALUES (%(name)s, %(ssn)s, %(email)s, %(phoneNumber)s)
                     RETURNING buyer_id;"""
        inserted_buyer_id: int = self.__database_connection.insert(command, buyer_dict)
        self.__database_connection.commit()
        return inserted_buyer_id

    def get_buyer(self, buyer_id: int) -> Union[Buyer, EmptyModel]:
        id_dict = {'buyer_id': buyer_id}
        command = """SELECT * FROM buyer
                     WHERE buyer_id = %(buyer_id)s;"""
        buyer_from_db = self.__database_connection.fetch(command, id_dict)
        if buyer_from_db is not None:
            return Buyer(
                name=buyer_from_db[0],
                ssn=buyer_from_db[1],
                email=buyer_from_db[2],
                phoneNumber=buyer_from_db[3]
            )
        return EmptyModel()
