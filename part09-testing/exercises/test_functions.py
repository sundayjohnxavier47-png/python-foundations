

import pytest
from calculator import add, subtract, divide


def test_add():
    assert add(5, 5) == 10
    assert add(-3, 4) == 1

def test_subtract():
    assert subtract(8, 4) == 4
    assert subtract(5, 7) == -2

def test_divide():
    assert divide(6, 3) == 2
    assert divide(15, 5) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)