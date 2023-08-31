from lib.user import User
from lib.booking import Booking


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
