import pytest


@pytest.fixture()
def default_square():
    square = Square(5)
    yield square
    del square


@pytest.fixture()
def default_rectangle():
    rectangle = Rectangle(5, 7)
    yield rectangle
    del rectangle


@pytest.fixture()
def default_triangle():
    triangle = Triangle(1, 2, 3)
    yield triangle
    del triangle


@pytest.fixture()
def default_circle():
    circle = Circle(2)
    yield circle
    del circle
