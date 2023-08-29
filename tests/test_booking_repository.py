from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date


def test_get_all_records(db_connection):
    db_connection.seed("seeds/MAKERSBNB_PROJECT.sql")
    repository = BookingRepository(db_connection)
    bookings = repository.all()
    assert bookings == [
        Booking(1, date(2023, 8, 10), date(2023, 8, 12), 400.00, 1, 2),
        Booking(2, date(2023, 7, 25), date(2023, 7, 27), 500.00, 2, 4),
        Booking(3, date(2023, 6, 1), date(2023, 6, 7), 600.00, 3, 3)
    ]


def test_create(db_connection):
    db_connection.seed("seeds/MAKERSBNB_PROJECT.sql")
    repository = BookingRepository(db_connection)
    repository.create(
        Booking(None, date(2022, 7, 11), date(2022, 7, 14), 800.00, 1, 4))
    bookings = repository.all()
    assert bookings == [
        Booking(1, date(2023, 8, 10), date(2023, 8, 12), 400.00, 1, 2),
        Booking(2, date(2023, 7, 25), date(2023, 7, 27), 500.00, 2, 4),
        Booking(3, date(2023, 6, 1), date(2023, 6, 7), 600.00, 3, 3),
        Booking(4, date(2022, 7, 11), date(2022, 7, 14), 800.00, 1, 4)
    ]


def test_find_booking_by_id(db_connection):
    db_connection.seed("seeds/MAKERSBNB_PROJECT.sql")
    repository = BookingRepository(db_connection)
    booking = repository.find(2)
    assert booking == Booking(2, date(2023, 7, 25),
                              date(2023, 7, 27), 500.00, 2, 4)
