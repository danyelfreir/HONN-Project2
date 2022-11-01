from typing import Tuple

import psycopg2

from persistence.db_config import DbConfig


class PostgresConnection:
    def __init__(self, db_config: DbConfig) -> None:
        self.__conn: psycopg2.connection = psycopg2.connect(**db_config.dict())

    def insert(self, sql: str, data: dict) -> int:
        cursor = self.__conn.cursor()
        cursor.execute(sql, data)
        return cursor.fetchone()[0]

    def fetch(self, sql, merchant_id: dict) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(sql, merchant_id)
        try:
            return cursor.fetchone()
        except psycopg2.ProgrammingError:
            return ()

    def commit(self) -> None:
        self.__conn.commit()
