from lib.user import User
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.space import Space
from flask import flash,redirect

import re

class UserRepository:
    def __init__(self, db_connection) -> None:
        self._connection = db_connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["email"],
                        row["password"], row["phone_number"])
            users.append(item)
        return users

    def create(self, user):
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
        password_regex = re.compile(password_pattern)

        if not re.fullmatch(password_regex, user.password):
            flash("Invalid password. Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            return redirect('/signup')

        rows = self._connection.execute('INSERT INTO users (name, email, password, phone_number) VALUES (%s, %s, %s, %s) RETURNING id', [
                                        user.name, user.email, user.password, user.phone_number])
        row = rows[0]
        user.id = row['id']
        return user

    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"],
                    row["password"], row["phone_number"])
    
    def find_by_email(self, user_email):
        rows = self._connection.execute(
            'SELECT * from users WHERE email = %s', [user_email])
        row = rows[0]
        return User(row["id"], row["name"], row["email"],
                    row["password"], row["phone_number"])
    
    def find_user_with_bookings(self, user_id):
        # Needs updating to return bookings and spaces along with the user
        user = self.find(user_id)
        rows = self._connection.execute(
            'SELECT bookings.id as booking_id, start_date, end_date, total_price, confirmed, space_id, spaces.name, spaces.address, spaces.price, spaces.description, spaces.image_url From bookings JOIN spaces on bookings.space_id = spaces.id WHERE bookings.user_id = %s', [user_id])
        
        bookings = []
        for row in rows:
            booking = Booking(row['booking_id'], row['start_date'], row['end_date'], row['total_price'], user.id, row['space_id'], row['confirmed'])
            booking.space_name = row['name']
            booking.space_address = row['address']
            bookings.append(booking)
        user.bookings = bookings
        return user
    
    def find_with_spaces_and_bookings(self, user_id):
        user = self.find(user_id)
        rows = self._connection.execute(
            'SELECT users.id, users.name as user_name, users.email, users.password, users.phone_number, spaces.id AS space_id, spaces.name AS space_name, spaces.description, spaces.price, spaces.user_id, spaces.image_url FROM users JOIN spaces ON users.id = spaces.user_id WHERE users.id = %s', [user_id])
        spaces = []
        for row in rows:
            print(row)
            space = Space(row['space_id'], row['space_name'], row['price'], row['description'], row['user_id'], row['image_url'])
            spaces.append(space)
        # row = rows[0]
        # user = User(row['id'], row['user_name'], row['email'], row['password'], row['phone_number'])
        user.spaces = spaces

        rows = self._connection.execute('SELECT * from bookings WHERE user_id = %s', [user_id])
            # 'SELECT users.id, users.email, users.password, bookings.id AS booking_id, bookings.start_date, bookings.end_date, bookings.confirmed, bookings.booked_by, bookings.space_id FROM users JOIN bookings ON users.id = bookings.id WHERE users.id = %s', [user_id])
        bookings = []
        booking_repository = BookingRepository(self._connection)
        for row in rows:
            booking_id = row['id']
            booking = booking_repository.find(booking_id)
            bookings.append(booking)
        user.bookings = bookings
        print(user.bookings)
        print(user)
        return user