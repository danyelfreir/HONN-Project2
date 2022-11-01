import sqlite3


class Database:
    def __init__(self) -> None:
        self._connection = sqlite3.connect('./data/payments.db')
        self._cursor = self._connection.cursor()
        self._create_table()

    def _create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS payments(
            order_id INTEGER PRIMARY KEY,
            success BOOLEAN)"""
        self._cursor.execute(sql)

    def insert(self, order_id, success):
        sql = "INSERT INTO payments VALUES (?, ?)"
        self._cursor.execute(sql, (order_id, success))
        self._connection.commit()

    def __del__(self):
        self._connection.close()
