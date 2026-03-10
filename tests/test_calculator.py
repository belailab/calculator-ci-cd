import pytest
from app.calculator import Calculator

calc = Calculator()


def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.subtract(5, 3) == 2


def test_multiply():
    assert calc.multiply(4, 5) == 20


def test_divide():
    assert calc.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)


def test_power():
    assert calc.power(2, 3) == 8


def test_sqrt():
    assert calc.sqrt(16) == 4


def test_sqrt_negative():
    with pytest.raises(ValueError):
        calc.sqrt(-4)


def test_quadratic():
    roots = calc.quadratic(1, -3, 2)
    assert roots == (2.0, 1.0)

