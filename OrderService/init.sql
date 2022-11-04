CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY ,
    product_id INTEGER NOT NULL,
    merchant_id INTEGER NOT NULL,
    buyer_id INTEGER NOT NULL,
    card_number VARCHAR(255) NOT NULL,
    total_price REAL NOT NULL
);