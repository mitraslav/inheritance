#pytest.raises()

def divide_numbers(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b

import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(1, 0)

def check_value(value: int) -> None:
    if value <= 0:
        raise ValueError('Value must be positive')

# код в файле test_funcs.py
import pytest
from funcs import check_value

def test_value_error():
    with pytest.raises(ValueError, match='Value must be positive'):
        check_value(-1)