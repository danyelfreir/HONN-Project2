CREATE TABLE merchant(merchant_id SERIAL PRIMARY KEY,
                      name VARCHAR(255) NOT NULL,
                      ssn VARCHAR(255) NOT NULL,
                      email VARCHAR(255) NOT NULL,
                      phone_number VARCHAR(255) NOT NULL,
                      allows_discount BOOLEAN NOT NULL);