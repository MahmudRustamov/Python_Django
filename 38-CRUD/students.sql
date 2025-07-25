CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_year INTEGER,
    grade INTEGER,
    graduated BOOLEAN DEFAULT FALSE
);