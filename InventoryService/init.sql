CREATE TABLE product(product_id SERIAL PRIMARY KEY,
                     merchant_id INTEGER NOT NULL,
                     name VARCHAR(255) NOT NULL,
                     price REAL NOT NULL,
                     quantity INTEGER NOT NULL,
                     reserved INTEGER NOT NULL);