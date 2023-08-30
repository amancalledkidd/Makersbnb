DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;





CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    phone_number VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) ,
    address VARCHAR(50) ,
    price FLOAT,
    description VARCHAR(125),
    user_id INT,
    image_url TEXT,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    start_date date,
    end_date date,
    total_price float,
    user_id int,
    space_id int,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_space FOREIGN KEY (space_id) REFERENCES spaces(id)
);

INSERT INTO users (name, email, password, phone_number) VALUES
('Rikie Patrick', 'rikie@gmail.com', 'password123', '01234567890'),
('Muhammad Mehmood', 'muhammad@gmail.com', 'makers321', '09876543210'),
('Kumani Kidd', 'kumani@makers.com', 'coding45!', '01111111111'),
('Yasien Watkin', 'yasien@makers.com', 'binaryhustler1', '05556667777');


INSERT INTO spaces (name, address, price, description, user_id, image_url) values ('Lind', 'Suite 17', 4.53, 'value-added', 1, 'https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');
INSERT INTO spaces (name, address, price, description, user_id, image_url) values ('Therese', 'Apt 1847', 4.33, 'coherent', 2, 'https://images.pexels.com/photos/3958958/pexels-photo-3958958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');
INSERT INTO spaces (name, address, price, description, user_id, image_url) values ('Kenn', 'PO Box 66640', 5.77, 'moderator', 3, 'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');
INSERT INTO spaces (name, address, price, description, user_id, image_url) values ('Abey', 'Suite 61', 0.91, 'Configurable', 4, 'https://images.pexels.com/photos/164558/pexels-photo-164558.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');
INSERT INTO spaces (name, address, price, description, user_id, image_url) values ('Elna', 'Room 450', 5.97, 'Visionary', 4, 'https://images.pexels.com/photos/7031405/pexels-photo-7031405.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');

INSERT INTO bookings (start_date, end_date, total_price, user_id, space_id) VALUES
('2023-08-10', '2023-08-12', 400.00, 1, 2),
('2023-07-25', '2023-07-27', 500.00, 2, 4),
('2023-06-01', '2023-06-07', 600.00, 3, 3);