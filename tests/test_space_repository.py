from lib.space_repository import *
from lib.space import *
import pytest


def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/MAKERSBNB_PROJECT.sql')
    repo = SpaceRepository(db_connection)
    assert repo.all() == [Space(1, 'Lind', 'Suite 17', 4.53, 'value-added', 1), 
    Space(2,'Therese', 'Apt 1847', 4.33, 'coherent', 2),
    Space(3,'Kenn', 'PO Box 66640', 5.77, 'moderator', 3), 
    Space(4,'Abey', 'Suite 61', 0.91, 'Configurable', 4), 
    Space(5,'Elna', 'Room 450', 5.97, 'Visionary', 4)]

def test_get_find_spaces(db_connection):
    db_connection.seed('seeds/MAKERSBNB_PROJECT.sql')
    repo = SpaceRepository(db_connection)
    assert repo.find(1) == Space(1, 'Lind', 'Suite 17', 4.53, 'value-added', 1)

def test_get_delete_spaces(db_connection):
    db_connection.seed('seeds/MAKERSBNB_PROJECT.sql')
    repo = SpaceRepository(db_connection)
    repo.delete(1)
    assert repo.all() == [
    Space(2,'Therese', 'Apt 1847', 4.33, 'coherent', 2),
    Space(3,'Kenn', 'PO Box 66640', 5.77, 'moderator', 3), 
    Space(4,'Abey', 'Suite 61', 0.91, 'Configurable', 4), 
    Space(5,'Elna', 'Room 450', 5.97, 'Visionary', 4)]

def test_get_create_spaces(db_connection):
    db_connection.seed('seeds/MAKERSBNB_PROJECT.sql')
    repo = SpaceRepository(db_connection)
    repo.create(Space(None, 'John', '123 Road', 10.11, 'coping',2))
    assert repo.all() == [
    Space(1, 'Lind', 'Suite 17', 4.53, 'value-added', 1),
    Space(2,'Therese', 'Apt 1847', 4.33, 'coherent', 2),
    Space(3,'Kenn', 'PO Box 66640', 5.77, 'moderator', 3), 
    Space(4,'Abey', 'Suite 61', 0.91, 'Configurable', 4), 
    Space(5,'Elna', 'Room 450', 5.97, 'Visionary', 4),
     Space(6,'John', '123 Road', 10.11, 'coping',2)
    ]

def test_get_update_spaces(db_connection):
    db_connection.seed('seeds/MAKERSBNB_PROJECT.sql')
    repo = SpaceRepository(db_connection)
    post = repo.find(1)
    post.price = 3.51
    assert repo.update(post) is None
    assert repo.all() == [
    Space(1, 'Lind', 'Suite 17', 3.51, 'value-added', 1),
    Space(2,'Therese', 'Apt 1847', 4.33, 'coherent', 2),
    Space(3,'Kenn', 'PO Box 66640', 5.77, 'moderator', 3), 
    Space(4,'Abey', 'Suite 61', 0.91, 'Configurable', 4), 
    Space(5,'Elna', 'Room 450', 5.97, 'Visionary', 4)
    ]