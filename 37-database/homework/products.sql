""" products jadvalini yarating, bu jadvalda mahsulot nomi, toifasi, zaxiradagi
    soni va mahsulot faol (boolean) ekanligini bildiruvchi ustun boâ€˜lsin."""

    CREATE TABLE products (
        id SERIAL PRIMARY KEY,
        product_name VARCHAR(150),
        product_type VARCHAR(100),
        quantity smallint NOT NULL,
        active_product BOOLEAN
    );