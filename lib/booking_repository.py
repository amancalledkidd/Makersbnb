from lib.booking import Booking
from lib.space_repository import SpaceRepository

class BookingRepository:
    def __init__(self, db_connection) -> None:
        self._connection = db_connection

    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        space_repository = SpaceRepository(self._connection)
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["start_date"], row["end_date"],
                           row["total_price"], row["user_id"], row["space_id"], row['confirmed'])
            item.space = space_repository.find(item.space_id)
            bookings.append(item)
            print(item)
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
        booking = Booking(row["id"], row["start_date"], row["end_date"],
                       row["total_price"], row["user_id"], row["space_id"], row['confirmed'])
        space_repository = SpaceRepository(self._connection)
        booking.space = space_repository.find(booking.space_id)
        return booking
    
    def find_by_space_id(self, space) -> list[Booking]:
        rows = self._connection.execute(
            'SELECT * from bookings WHERE space_id = %s', [space.id])
        bookings = []
        for row in rows:
            booking = Booking(row["id"], row["start_date"], row["end_date"],
                       row["total_price"], row["user_id"], row["space_id"], row['confirmed'])
            bookings.append(booking)
        space.bookings = bookings
        return space
    
    def confirm(self, booking):
        self._connection.execute('UPDATE bookings SET confirmed = TRUE WHERE id = %s', [booking.id])
        return None
    
    def reject(self, booking):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [booking.id])
        return None
