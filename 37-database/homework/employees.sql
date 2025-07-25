"""employees nomli jadval tuzing, u xodim ID raqami, toâ€˜liq ism, lavozimi,
    ishga kirgan sana va oylik maosh ustunlarini oâ€˜z ichiga olsin."""

CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(300),
    position VARCHAR(100),
    accepted_date DATE,
    salary INT
);