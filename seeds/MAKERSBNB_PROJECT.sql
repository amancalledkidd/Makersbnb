DROP TABLE IF EXISTS spaces

CREATE TABLE spaces(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    price FLOAT NOT NULL,
    description VARCHAR(125) NOT NULL,
    user_id INT FOREIGN KEY
    constrain fk_user foreign key(user_id)references users(id)

)

INSERT INTO MAKERSBNB_PROJECT (id, name, address, price, description, user_id) values (1, 'Lind', 'Suite 17', '£4.53', 'value-added', 1);
INSERT INTO MAKERSBNB_PROJECT (id, name, address, price, description, user_id) values (2, 'Therese', 'Apt 1847', '£4.33', 'coherent', 2);
INSERT INTO MAKERSBNB_PROJECT (id, name, address, price, description, user_id) values (3, 'Kenn', 'PO Box 66640', '£5.77', 'moderator', 3);
INSERT INTO MAKERSBNB_PROJECT (id, name, address, price, description, user_id) values (4, 'Abey', 'Suite 61', '£0.91', 'Configurable', 4);
INSERT INTO MAKERSBNB_PROJECT (id, name, address, price, description, user_id) values (5, 'Elna', 'Room 450', '£5.97', 'Visionary', 5);
