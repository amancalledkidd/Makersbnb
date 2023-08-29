from lib.space import *
import pytest

def test_init():
    space = Space(1, 'Lind', 'Suite 17', 4.53, 'value_added', 1)
    assert space.id == 1
    assert space.name == 'Lind'
    assert space.address == 'Suite 17'
    assert space.price == 4.53
    assert space.description == 'value_added'
    assert space.user_id == 1

def test_spaces_eq():
    space = Space(1, 'Lind', 'Suite 17', 4.53, 'value_added', 1)
    spaceJam = Space(1, 'Lind', 'Suite 17', 4.53, 'value_added', 1)
    assert space == spaceJam
    space2 = Space(1, 'Lind', 'Suite 173', 43.53, 'value_not_added', 1)
    spaceJam2 = Space(1, 'Lind', 'Suite 17', 4.53, 'value_added', 1)
    assert space2.name == spaceJam2.name

def test_spaces_repr():
    space = Space(1, 'Lind', 'Suite 17', 4.53, 'value_added', 1)
    assert  str(space) == "Space(1, Lind, Suite 17, 4.53, value_added, 1)"