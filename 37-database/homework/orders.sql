"""orders jadvali yarating, u buyurtma ID, mijoz ID, mahsulot ID, buyurtma sanasi
    va umumiy summa ustunlarini oâ€˜z ichiga olsin (umumiy summani aniq decimal turida saqlang)."""


CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    order_date DATE,
    total_price DECIMAL(10, 2)
);