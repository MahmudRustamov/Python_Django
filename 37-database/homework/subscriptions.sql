"""subscriptions nomli jadval yarating, unda foydalanuvchi IDsi,
    obuna turi (masalan: "basic", "premium"), boshlanish sanasi, tugash sanasi (DATE), va faol (boolean) ustunlari boâ€˜lsin."""


CREATE TABLE subscriptions (
    user_id SERIAL PRIMARY KEY,
    subscription_type VARCHAR(50) CHECK (subscription_type IN ('basic', 'premium')),
    start_time DATE,
    end_date DATE
    is_active BOOLEAN
);