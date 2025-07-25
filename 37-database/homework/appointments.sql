"""appointments jadvalini tuzing, unda uchrashuv IDsi, bemor ismi, shifokor ismi,
    uchrashuv sanasi va vaqti, va davomiyligi (interval turi) boâ€˜lsin."""


CREATE TABLE appointments (
    meeting_id SERIAL PRIMARY KEY,
    guest_name VARCHAR(100),
    doctor_name VARCHAR(100),
    appoinment_time TIMESTAMP
    duration INTERVAL,
);