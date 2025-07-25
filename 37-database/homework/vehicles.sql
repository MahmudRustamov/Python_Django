"""vehicles nomli jadval yarating, unda transport vositasi IDsi, ishlab chiqaruvchi,
    model, yil, roâ€˜yxatdan oâ€˜tgan sana va kuzatuv uchun UUID ustuni boâ€˜lsin."""


CREATE TABLE vehicles (
    id SERIAL PRIMARY KEY,
    manufacturer VARCHAR(100) NOT NULL, 
    model VARCHAR(50),
    year SMALLINT,
    registration_date DATE,
    tracking_uuid UUID DEFAULT gen_random_uuid()
);