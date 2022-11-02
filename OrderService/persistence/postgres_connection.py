from typing import Tuple

import psycopg2

from persistence.db_config import DbConfig


class PostgresConnection:
    def __init__(self, db_config: DbConfig) -> None:
        self.__conn: psycopg2.connection = psycopg2.connect(**db_config.dict())
        self.__setup_db()

    def insert(self, sql: str, data: dict) -> int:
        cursor = self.__conn.cursor()
        cursor.execute(sql, data)
        return cursor.fetchone()[0]

    def fetch(self, sql, order_id: dict) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(sql, order_id)
        try:
            return cursor.fetchone()
        except psycopg2.ProgrammingError:
            return ()

    def commit(self) -> None:
        self.__conn.commit()

    def __setup_db(self) -> None:
        cursor = self.__conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                                order_id SERIAL PRIMARY KEY ,
                                product_id INTEGER NOT NULL,
                                merchant_id INTEGER NOT NULL,
                                buyer_id INTEGER NOT NULL,
                                card_number VARCHAR(255) NOT NULL,
                                total_price REAL
                                );"""
        )
        self.__conn.commit()
