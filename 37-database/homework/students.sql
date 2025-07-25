"""students jadvalini tuzing, unda talabalar ID raqami (avto-inkrement), ism,
    tugâ€˜ilgan sana, sevimli fanlar (array koâ€˜rinishida) va oâ€˜qishga kirgan sana boâ€˜lsin."""

    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(150),
        birth_date DATE,
        fav_subjects TEXT[],
        accepted_date DATE
    );
