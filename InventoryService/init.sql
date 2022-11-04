CREATE TABLE product(product_id SERIAL PRIMARY KEY,
                        merchantId INTEGER NOT NULL,
                        productName VARCHAR(255) NOT NULL,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL,
                        reserved INTEGER);