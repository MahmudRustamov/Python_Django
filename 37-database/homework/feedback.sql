""" feedbacks nomli jadval yarating, foydalanuvchi ismi, baho (1 dan 5 gacha),
    sharh (text), va yuborilgan sana/vaqt (timestamp) ustunlarini oâ€˜z ichiga olsin."""

CREATE TABLE feedbacks (
    user_name VARCHAR(150),
    grade SMALLINT CHECK (grade BETWEEN 1 AND 5),
    feedback TEXT,
    send_time TIMESTAMP
);