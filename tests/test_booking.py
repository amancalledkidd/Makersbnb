from lib.booking import Booking
from datetime import date


def test_booking_initialises():
    start_date = date(2023, 2, 10)
    end_date = date(2023, 2, 12)
    booking = Booking(1, start_date, end_date, 500.00, 1, 2)
    assert booking.id == 1
    assert booking.start_date == start_date
    assert booking.end_date == end_date
    assert booking.total_price == 500.00
    assert booking.user_id == 1
    assert booking.space_id == 2


def test_bookings_are_equal():
    start_date = date(2023, 2, 10)
    end_date = date(2023, 2, 12)
    booking1 = Booking(1, start_date, end_date, 500.00, 1, 2)
    booking2 = Booking(1, start_date, end_date, 500.00, 1, 2)
    assert booking1 == booking2


def test_format_str():
    start_date = date(2023, 2, 10)
    end_date = date(2023, 2, 12)
    booking = Booking(1, start_date, end_date, 500.00, 1, 2)
    assert str(
        booking) == "Booking(1, 2023-02-10 to 2023-02-12, £500.00, 1, 2)"

# TODO: Add test to check end date is after start date, price is positive float, date is not in the past
