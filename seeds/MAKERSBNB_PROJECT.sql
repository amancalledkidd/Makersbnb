DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    phone_number VARCHAR(255)
);

INSERT INTO users (name, email, password, phone_number) VALUES
('Rikie Patrick', 'rikie@gmail.com', 'password123', '01234567890'),
('Muhammad Mehmood', 'muhammad@gmail.com', 'makers321', '09876543210'),
('Kumani Kidd', 'kumani@makers.com', 'coding45!', '01111111111'),
('Yasien Watkin', 'yasien@makers.com', 'binaryhustler1', '05556667777');

-- insert into MAKERSBNB_PROJECT (id, start_date, end_date, total_price, description, user_id, space_id) values (1, '7/22/2023', '3/28/2023', '£4.28', 'De-engineered', 1, 1);
-- insert into MAKERSBNB_PROJECT (id, start_date, end_date, total_price, description, user_id, space_id) values (2, '4/16/2023', '1/18/2023', '£5.89', 'attitude-oriented', 2, 2);
-- insert into MAKERSBNB_PROJECT (id, start_date, end_date, total_price, description, user_id, space_id) values (3, '10/15/2022', '9/11/2022', '£6.20', 'toolset', 3, 3);
-- insert into MAKERSBNB_PROJECT (id, start_date, end_date, total_price, description, user_id, space_id) values (4, '2/10/2023', '6/1/2023', '£7.21', 'Distributed', 4, 4);
-- insert into MAKERSBNB_PROJECT (id, start_date, end_date, total_price, description, user_id, space_id) values (5, '7/28/2023', '11/8/2022', '£3.22', 'Stand-alone', 5, 5);
