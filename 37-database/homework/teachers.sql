""" teachers jadvalini tuzing, u yerda o'qituvchi IDsi (avto-inkrement),
    ism, mutaxassislik, yillik tajribasi (integer), va tug'ilgan sanasi bo'lsin."""


CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    full_name VARCHAR(200),
    specialty VARCHAR(100)
    experience INT,
    birth_date DATE,
);
