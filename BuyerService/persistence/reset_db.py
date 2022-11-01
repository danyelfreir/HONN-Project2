import psycopg2


def create_table():
	commands = (
			"DROP TABLE IF EXISTS buyer",
		"""CREATE TABLE buyer(name VARCHAR(255) NOT NULL,
			ssn VARCHAR(255) NOT NULL,
			email VARCHAR(255) NOT NULL,
			phone_number VARCHAR(255) NOT NULL,
			buyer_id INT GENERATED ALWAYS AS IDENTITY);
		)"""
	)
	