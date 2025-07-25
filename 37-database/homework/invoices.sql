"""invoices nomli jadval yarating, unda quyidagi ustunlar bo'lsin:
    hisob-faktura raqami, mijoz ismi, sana, umumiy summa (decimal), va to'langanmi (boolean)."""

CREATE TABLE invoices (
    invoice_number SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    invoice_date DATE,
    total_amount DECIMAL,
    is_paid BOOLEAN
);
