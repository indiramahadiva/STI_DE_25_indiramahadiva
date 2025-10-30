from pytest import raises
from triangle import Triangle


def test_valid_init():
    triangle = Triangle(base=5, height=2, height_2=7)
    assert triangle.base == 5 and triangle.height == 2 or triangle.height_2 == 7


def test_negative_base_fail():
    with raises(ValueError):
        Triangle(base=-1, height=2, height_2=6)


def test_negative_height_fail():
    with raises(ValueError):
        Triangle(base=-4, height=-2, height_2=-6)


def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Triangle(base="1", height=1, height_2="4")


def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Triangle(height=True)


def test_zero_base_fail():
    with raises(ValueError):
        Triangle(base=0, height=1, height_2=0)


def test_area_validation():
    triangle = Triangle(base=5, height=2, height_2=1)
    assert 0.5 * triangle.base * triangle.height == 5
