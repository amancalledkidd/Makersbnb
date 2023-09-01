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
    description text,
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
    confirmed boolean DEFAULT FALSE,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_space FOREIGN KEY (space_id) REFERENCES spaces(id)
);

INSERT INTO users (name, email, password, phone_number) VALUES
('Rikie Patrick', 'rikie@gmail.com', 'password123', '01234567890'),
('Muhammad Mehmood', 'muhammad@gmail.com', 'makers321', '09876543210'),
('Kumani Kidd', 'kumani@makers.com', 'coding45!', '01111111111'),
('Yasien Watkin', 'yasien@makers.com', 'binaryhustler1', '05556667777'),
('Renee McCook', 'rmccook0@wunderground.com', 'vQ8\B(@z4p', '07384825288'),
('Ives Frondt', 'ifrondt1@edublogs.org', 'pR7|2T<q', '06053202672'),
('Scot Collinge', 'scollinge2@networkadvertising.org', 'aO1@z4&3lY', '07425323400'),
('Adelina Seymour', 'aseymour3@bbb.org', 'eL1"i(2umnFhZe1', '04023882391'),
('Constancia McNae', 'cmcnae4@time.com', 'fP6|+kzu7L2qZC', '01089978415'),
('Elnore Roly', 'eroly5@arstechnica.com', 'rL3,M}Gf', '03304347211'),
('Mallissa Fielden', 'mfielden6@salon.com', 'tM2(zg8_}T''w9U`', '09565247480'),
('Davon Ankers', 'dankers7@cargocollective.com', 'nR6)~@l4', '09068651679'),
('Erminia Noad', 'enoad8@lulu.com', 'qU8%>2\0)ReN)P', '05108001929'),
('Chucho Downs', 'cdowns9@google.com', 'fM7~FfM(lOS''co)', '09145559877'),
('Dotty Lovelock', 'dlovelocka@multiply.com', 'nU4%!zlO`nD>jmkZ', '04359481367'),
('Conny Clowes', 'cclowesb@europa.eu', 'xN5.o%IwBT"L''3l', '02559429275'),
('Rudyard Autin', 'rautinc@smh.com.au', 'xR5,L$2=Y7gfO0', '09682380775'),
('Kearney Aurelius', 'kaureliusd@bandcamp.com', 'kP6"hJsAT', '01067258995'),
('Maurise Bunting', 'mbuntinge@tmall.com', 'uJ0,)S}OuN.r', '09973755425'),
('Vic Bonnet', 'vbonnetf@booking.com', 'lI9&Vc/oUNtx', '09868728908');

INSERT INTO spaces (name, address, price, description, user_id, image_url) VALUES
('Cityscape Haven', '42 Oak Street, London, SW1A 1AA', '458.32', 'Experience luxury in the heart of the city! Our spacious apartment offers stunning views of the skyline, modern amenities, and easy access to all the best restaurants and attractions.', '7', 'https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
('Secluded Retreat', '17 Maple Avenue, Manchester, M1 1AA', '742.81', 'Escape to our charming countryside cottage for a peaceful retreat. Enjoy walks through lush gardens, cozy evenings by the fireplace, and breathtaking sunsets over the rolling hills.', '10', 'https://images.pexels.com/photos/3958958/pexels-photo-3958958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Historic Elegance', '63 Pine Lane, Edinburgh, EH1 1AA', '773.64', 'Immerse yourself in history with a stay in our beautifully restored historic home. Located in a quaint neighborhood, you''ll be steps away from local cafes, museums, and historic sites.', '11', 'https://images.pexels.com/photos/164558/pexels-photo-164558.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Urban Oasis', '101 Oak Street, London, SW1A 2BB', '298.15', 'Indulge in relaxation at our spa-inspired retreat. Unwind in the hot tub, pamper yourself with rejuvenating treatments, and enjoy the serene ambiance of our tranquil oasis.', '9', 'https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
('Tranquil Waters', '56 Maple Avenue, Manchester, M1 2BB', '712.56', 'Discover serenity at our mountain cabin. Surrounded by pristine nature, you can hike, stargaze, and roast marshmallows over the campfire for a perfect family getaway.', '18', 'https://images.pexels.com/photos/3958958/pexels-photo-3958958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Modern Urban Living', '19 Cedar Road, Birmingham, B1 3CC', '122.05', 'Unplug and unwind at our lakeside cabin. Fish, canoe, or simply lounge on the deck as you enjoy the tranquility of the water and the beauty of the surrounding forest.', '11', 'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Tropical Bliss', '39 Pine Lane, Edinburgh, EH1 2BB', '210.73', 'Live like a local in our vibrant urban loft. Situated in a trendy neighborhood, you''ll be steps away from artisanal coffee shops, lively street markets, and bustling nightlife.', '1', 'https://images.pexels.com/photos/164558/pexels-photo-164558.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Sunset Paradise', '8 Cedar Road, Birmingham, B1 1AA', '177.46', 'Stay in our beachfront paradise and fall asleep to the sound of the waves. This cozy bungalow offers direct access to the sandy shores and is perfect for a relaxing seaside getaway.', '18', 'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Countryside Comfort', '5 Elm Court, Glasgow, G1 3CC', '581.22', 'Discover the magic of our secluded cottage in the woods. Surrounded by trees and wildlife, it''s the perfect place to reconnect with nature and find peace and solitude.', '10', 'https://images.pexels.com/photos/7031405/pexels-photo-7031405.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Cultural Haven', '22 Pine Lane, Edinburgh, EH1 4DD', '58.97', 'Immerse yourself in local culture at our traditional villa. With authentic furnishings and a central courtyard, you''ll feel like a part of the community during your stay.', '11', 'https://images.pexels.com/photos/164558/pexels-photo-164558.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Skyline Serenade', '60 Oak Street, London, SW1A 4DD', '527.34', 'Stay in a castle fit for royalty! Our historic fortress offers opulent rooms, expansive gardens, and a taste of a bygone era with all the modern conveniences.', '18', 'https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
('Bohemian Hideaway', '22 Cedar Road, Birmingham, B1 2BB', '635.28', 'Escape to our rustic farmhouse for a taste of country life. You''ll have access to our private orchard, enjoy farm-to-table meals, and experience the joys of rural living.', '3', 'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Historic Gem', '31 Maple Avenue, Manchester, M1 4DD', '374.08', 'Experience the bohemian spirit of our artist''s loft. Filled with creativity and unique decor, this space is perfect for those seeking inspiration and a one-of-a-kind stay.', '15', 'https://images.pexels.com/photos/3958958/pexels-photo-3958958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Mountain Escape', '28 Elm Court, Glasgow, G1 1AA', '434.79', 'Experience the ultimate treehouse adventure! Our unique property is nestled among the treetops, offering stunning forest views, modern amenities, and a truly one-of-a-kind stay.', '10', 'https://images.pexels.com/photos/7031405/pexels-photo-7031405.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Serenity Cottage', '14 Elm Court, Glasgow, G1 2BB', '285.19', 'Find your own piece of paradise in our tropical villa. Lounge by the pool, sip cocktails on the terrace, and explore the nearby coral reefs for an unforgettable vacation.', '7', 'https://images.pexels.com/photos/7031405/pexels-photo-7031405.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Seaside Charm', '88 Maple Avenue, Manchester, M1 3CC', '657.77', 'Experience the charm of our historic townhouse. With period features and elegant decor, you''ll step back in time while enjoying all the modern comforts you need.', '9', 'https://images.pexels.com/photos/3958958/pexels-photo-3958958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Luxury Castle Retreat', '73 Oak Street, London, SW1A 3CC', '87.91', 'Stay in architectural wonder! Our modern glass house offers panoramic views, sleek design, and a connection to nature that will make your stay truly exceptional.', '19', 'https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
('Enchanted Forest Cabin', '47 Pine Lane, Edinburgh, EH1 3CC', '948.62', 'Relax in style at our designer apartment. Every corner is carefully curated for comfort and aesthetics, making it the perfect retreat after a day of urban exploration.', '2', 'https://images.pexels.com/photos/164558/pexels-photo-164558.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Alpine Wonderland', '9 Cedar Road, Birmingham, B1 4DD', '627.49', 'Escape to our lakeside chalet for a winter wonderland experience. Ski on nearby slopes, warm up by the fireplace, and soak in the breathtaking snowy views.', '8', 'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'),
('Eco-Friendly Haven', '75 Elm Court, Glasgow, G1 4DD', '801.12', 'Unwind at our eco-friendly retreat. Surrounded by lush gardens and sustainable features, you can relax knowing your stay has a minimal environmental impact.', '4', 'https://images.pexels.com/photos/7031405/pexels-photo-7031405.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');


INSERT INTO bookings (start_date, end_date, total_price, user_id, space_id) VALUES
('2023-08-10', '2023-08-12', 400.00, 1, 2),
('2023-07-25', '2023-07-27', 500.00, 2, 4),
('2023-06-01', '2023-06-07', 600.00, 3, 3),
('2023-02-20', '2022-09-29', 755.66, 18, 4),
('2022-11-27', '2023-03-29', 2213.19, 8, 9),
('2022-10-09', '2023-05-17', 978.61, 10, 14),
('2023-04-24', '2022-10-18', 530.29, 11, 7),
('2023-04-03', '2023-02-15', 1904.8, 16, 9),
('2022-10-04', '2022-12-20', 1560.14, 4, 19),
('2022-12-05', '2022-10-04', 144.21, 3, 9),
('2023-01-10', '2023-06-12', 286.28, 13, 1),
('2023-06-14', '2023-05-14', 961.13, 14, 5),
('2022-12-10', '2023-08-26', 2312.9, 10, 11),
('2022-11-11', '2022-12-15', 1993.72, 11, 15),
('2023-03-14', '2022-12-16', 1376.36, 4, 1),
('2023-02-05', '2022-11-08', 2190.65, 1, 9),
('2022-09-19', '2023-08-24', 1989.76, 15, 20),
('2022-11-04', '2023-06-26', 1733.34, 19, 2),
('2023-06-17', '2023-05-14', 1898.47, 9, 17),
('2022-10-24', '2022-11-29', 1800.33, 19, 2),
('2023-04-09', '2022-11-12', 661.34, 20, 6),
('2022-10-21', '2022-10-18', 523.63, 16, 4),
('2022-10-10', '2023-07-17', 2211.51, 1, 6),
('2023-04-04', '2022-10-21', 2746.97, 8, 1),
('2022-10-26', '2022-10-15', 1556.94, 7, 9),
('2023-04-22', '2023-06-16', 1702.58, 18, 15),
('2023-03-06', '2023-05-31', 65.28, 20, 13),
('2022-11-04', '2022-09-10', 1789.06, 10, 17),
('2022-10-01', '2022-12-20', 489.62, 9, 4),
('2023-04-03', '2022-11-19', 1717.21, 20, 8),
('2023-02-16', '2022-10-11', 1717.15, 11, 13),
('2022-11-21', '2023-05-16', 1308.09, 3, 17),
('2023-05-04', '2023-02-27', 124.65, 9, 7),
('2022-12-31', '2023-03-07', 781.5, 19, 18),
('2022-10-11', '2022-11-11', 810.23, 5, 4),
('2023-05-18', '2023-06-19', 2628.36, 6, 4),
('2022-10-30', '2022-10-14', 1504.12, 2, 2),
('2023-05-01', '2023-01-03', 574.63, 5, 17),
('2023-07-15', '2023-02-20', 2857.55, 12, 19),
('2022-12-16', '2023-07-06', 532.99, 13, 2),
('2023-06-06', '2023-08-07', 2635.82, 18, 16),
('2023-07-13', '2023-08-30', 838.48, 6, 11),
('2022-12-06', '2022-12-18', 2220.37, 13, 19),
('2023-03-08', '2022-12-05', 2976.31, 10, 18),
('2022-12-18', '2023-08-19', 691.14, 14, 20),
('2023-01-03', '2023-04-01', 2593.36, 15, 2),
('2023-01-25', '2023-03-21', 2220.14, 10, 13),
('2022-09-01', '2023-08-12', 48.23, 11, 3),
('2023-08-10', '2023-03-04', 119.75, 14, 9),
('2023-01-13', '2022-09-26', 314.92, 10, 4),
('2023-07-23', '2023-06-25', 2999.85, 13, 11),
('2022-12-01', '2022-10-15', 906.41, 9, 10),
('2022-09-20', '2022-12-13', 1489.64, 14, 12);