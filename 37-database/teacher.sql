CREATE TABLE teacher (
    full_name VARCHAR(150) NOT NULL,
    age smallint check (age>0),
    gender BOOLEAN,
    subjects VARCHAR(50),
    email VARCHAR(120) NOT NULL,
    birth_date DATE NOT NULL,
    phone_number CHAR(13)
);