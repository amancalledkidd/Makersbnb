from lib.space_repository import *
from lib.space import *
import pytest


def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/MAKERSBNB_PROJECT.sql')
    repo = SpaceRepository(db_connection)
    assert repo.all() == [Space(1, 'Lind', 'Suite 17', 4.53, 'value-added', 1)]

def test_get_find_spaces(db_connection):
    db_connection.seed('seeds/MAKERSBNB_PROJECT.sql')
    repo = SpaceRepository(db_connection)
    assert repo.find(1) == Space(1, 'Lind', 'Suite 17', 4.53, 'value-added', 1)

# def test_get_delete_spaces(db_connection):
#     db_connection.seed('seeds/MAKERSBNB_PROJECT.sql')
#     repo = SpaceRepository(db_connection)
#     repo.delete(1)
#     assert repo.find(1) == 'Space not availiable'

# def test_get_create_spaces(db_connection):
#     db_connection.seed('seeds/MAKERSBNB_PROJECT.sql')
#     repo = SpaceRepository(db_connection)