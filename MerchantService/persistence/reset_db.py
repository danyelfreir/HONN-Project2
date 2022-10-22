import psycopg2


def create_table():
	commands = (
		"DROP TABLE IF EXISTS merchant",
		"""CREATE TABLE merchant (
			name VARCHAR(255) NOT NULL,
			ssn VARCHAR(255) NOT NULL,
			email VARCHAR(255) NOT NULL,
			phone_number VARCHAR(255) NOT NULL,
			allows_discount BOOLEAN NOT NULL
		)"""
	)
	