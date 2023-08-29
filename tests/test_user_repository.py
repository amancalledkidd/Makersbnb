from lib.user_repository import UserRepository
from lib.user import User


def test_get_all_records(db_connection):
    db_connection.seed("seeds/MAKERSBNB_PROJECT.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'Rikie Patrick', 'rikie@gmail.com',
             'password123', '01234567890'),
        User(2, 'Muhammad Mehmood', 'muhammad@gmail.com',
             'makers321', '09876543210'),
        User(3, 'Kumani Kidd', 'kumani@makers.com', 'coding45!', '01111111111'),
        User(4, 'Yasien Watkin', 'yasien@makers.com',
             'binaryhustler1', '05556667777'),
    ]


def test_create(db_connection):
    db_connection.seed("seeds/MAKERSBNB_PROJECT.sql")
    repository = UserRepository(db_connection)
    repository.create(
        User(None, 'Test Name', 'test@email.com', 'abcde12345', '09999999999'))
    users = repository.all()
    assert users == [
        User(1, 'Rikie Patrick', 'rikie@gmail.com',
             'password123', '01234567890'),
        User(2, 'Muhammad Mehmood', 'muhammad@gmail.com',
             'makers321', '09876543210'),
        User(3, 'Kumani Kidd', 'kumani@makers.com', 'coding45!', '01111111111'),
        User(4, 'Yasien Watkin', 'yasien@makers.com',
             'binaryhustler1', '05556667777'),
        User(5, 'Test Name', 'test@email.com', 'abcde12345', '09999999999')
    ]


def test_find_user_by_id(db_connection):
    db_connection.seed("seeds/MAKERSBNB_PROJECT.sql")
    repository = UserRepository(db_connection)
    user = repository.find(2)
    assert user == User(2, 'Muhammad Mehmood',
                        'muhammad@gmail.com', 'makers321', '09876543210')
