from lib.booking import Booking
from lib.space_repository import SpaceRepository

class BookingRepository:
    def __init__(self, db_connection) -> None:
        self._connection = db_connection

    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["start_date"], row["end_date"],
                           row["total_price"], row["user_id"], row["space_id"], row['confirmed'])
            bookings.append(item)
        return bookings

    def create(self, booking):
        rows = self._connection.execute('INSERT INTO bookings (start_date, end_date, total_price, user_id, space_id, confirmed) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', [
                                        booking.start_date, booking.end_date, booking.total_price, booking.user_id, booking.space_id, booking.confirmed])
        row = rows[0]
        booking.id = row['id']
        space_repository = SpaceRepository(self._connection)
        booking.space = space_repository.find(booking.space_id)
        return booking

    def find(self, booking_id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE id = %s', [booking_id])
        row = rows[0]
        return Booking(row["id"], row["start_date"], row["end_date"],
                       row["total_price"], row["user_id"], row["space_id"], row['confirmed'])
    
    # def find_booking_with_space(self, booking):
    #     rows = self._connection.execute(
    #         'SELECT * from spaces WHERE id = %s', [booking.space_id])
    #     row = rows[0]
    #     booking.space_name = row['name']
    #     booking.space_address = row['address']
    #     return booking
