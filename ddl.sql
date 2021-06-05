CREATE TABLE users (
    user_id INTEGER,
    first_name VARCHAR(155),
    last_name VARCHAR(155),
    email VARCHAR(155),
    city VARCHAR(155),
    state VARCHAR(155),
    date_joined DATE 
);

CREATE TABLE symbols (
    symbol_id INTEGER,
    symbol VARCHAR(155),
    date_added DATE,
    listed_at VARCHAR(155)
);

CREATE TABLE orders (
    order_id INTEGER,
    user_id INTEGER,
    symbol_id INTEGER,
    price INTEGER,
    quantity INTEGER,
    order_date DATE,
    buy_or_sell VARCHAR(155),
    order_status VARCHAR(155)
);
