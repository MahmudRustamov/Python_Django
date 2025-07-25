"""movies nomli jadval yarating, unda film nomi, rejissyor, chiqish sanasi, janr
    va reyting (bir oâ€˜nlik kasr koâ€˜rinishida) boâ€˜lsin."""


CREATE TABLE movies (
    film_name VARCHAR(200),
    film_director VARCHAR(200),
    release_date DATE,
    genre VARCHAR(50),
    rating DECIMAL(10, 1)
);
