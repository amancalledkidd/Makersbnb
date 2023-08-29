from lib.user import User


def test_user_initialises():
    user = User(1, 'Rikie Patrick', "rikie@gmail.com",
                "password123", "01234567890")
    assert user.id == 1
    assert user.name == 'Rikie Patrick'
    assert user.email == 'rikie@gmail.com'
    assert user.password == 'password123'
    assert user.phone_number == '01234567890'


def test_users_are_equal():
    user1 = User(1, 'Rikie Patrick', "rikie@gmail.com",
                 "password123", "01234567890")
    user2 = User(1, 'Rikie Patrick', "rikie@gmail.com",
                 "password123", "01234567890")
    assert user1 == user2


def test_format_str():
    user = User(1, 'Rikie Patrick', "rikie@gmail.com",
                "password123", "01234567890")
    assert str(user) == "User(1, Rikie Patrick, rikie@gmail.com, 01234567890)"

# TODO: Write more tests for name, email and phone validation
