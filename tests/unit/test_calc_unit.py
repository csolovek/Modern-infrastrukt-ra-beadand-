from src.calc import Calculator
import pytest

def test_add():
    c = Calculator()
    assert c.add(2, 3) == 5

def test_divide_ok():
    c = Calculator()
    assert c.divide(10, 2) == 5

def test_divide_by_zero():
    c = Calculator()
    with pytest.raises(ValueError):
        c.divide(1, 0)

