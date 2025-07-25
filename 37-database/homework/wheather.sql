"""weather_logs jadvalini yarating, unda log ID, sana, harorat
    (real turi), namlik (real turi), va izohlar (text) boâ€˜lsin."""


CREATE TABLE weather_logs (
    log_id SERIAL PRIMARY KEY,
    log_date DATE,
    temperature REAL,
    humidity REAL,
    comments TEXT
);