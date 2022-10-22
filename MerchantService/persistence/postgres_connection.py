import psycopg2
from typing import List, Tuple
from persistence.db_config import DbConfig

class PostgresConnection:
    def __init__(self, db_config: DbConfig) -> None:
        self.__conn: psycopg2.connection = psycopg2.connect(**db_config.dict())

    def insert(self, sql: str, data: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(sql, data)

    def fetch(self, sql, merchant_id: dict) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(sql, merchant_id)
        try:
            return cursor.fetchone()
        except psycopg2.ProgrammingError:
            return ()

    def commit(self) -> None:
        self.__conn.commit()
