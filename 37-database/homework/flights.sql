""" flights jadvalini tuzing, bu jadvalda reys raqami, manzil,
    uchish vaqti (TIMESTAMP), kelish vaqti, va parvoz davomiyligi (INTERVAL) boâ€˜lsin.
"""


CREATE TABLE flights (
    flight_id INT NOT NULL,
    addresss VARCHAR(100),
    flight_time TIMESTAMP,
    arrival_time TIMESTAMP,
    duration INTERVAL
);