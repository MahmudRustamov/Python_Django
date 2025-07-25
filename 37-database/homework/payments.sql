"""payments jadvalini tuzing, bu jadval toâ€˜lov IDsi, toâ€˜lovchi ismi,
    miqdori, toâ€˜lov usuli va vaqt belgisini (timestamp) oâ€˜z ichiga olsin."""


CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY, 
    payer_name VARCHAR(200),
    amount DECIMAL(10, 2),
    payment_method TEXT CHECK (payment_type IN ('cash', 'card', 'online'))
    created_at TIMESTAMP,
);