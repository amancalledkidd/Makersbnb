from lib.booking_repository import BookingRepository
from lib.booking import Booking
from lib.space_repository import SpaceRepository
from lib.space import Space
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
    booking_repository = BookingRepository(db_connection)
    space_repository = SpaceRepository(db_connection)
    start_date = date(2022, 7, 11)
    end_date = date(2022, 7, 14)
    booking = booking_repository.create(
        Booking(None, start_date, end_date, 800.00, 1, 4))
    space = Space('Abey', 'Suite 61', 0.91, 'Configurable', 4, 'https://images.pexels.com/photos/164558/pexels-photo-164558.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')
    bookings = booking_repository.all()
    assert bookings[3] == Booking(4, start_date, end_date, 800.00, 1, 4, False, space)


def test_find_booking_by_id(db_connection):
    db_connection.seed("seeds/MAKERSBNB_PROJECT.sql")
    repository = BookingRepository(db_connection)
    booking = repository.find(2)
    assert booking == Booking(2, date(2023, 7, 25),
                              date(2023, 7, 27), 500.00, 2, 4)
