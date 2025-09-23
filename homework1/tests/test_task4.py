import sys
import os
import pytest

# Add the src folder to the path so import works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task4 import calclulate_discount 

def test_discount_int():
    assert calclulate_discount(100, 20) == 80
    assert isinstance(calclulate_discount(100, 20), int) or isinstance(calclulate_discount(100, 20), float)

def test_discount_float():
    assert calclulate_discount(100.0, 12.5) == 87.5
    assert isinstance(calclulate_discount(100, 12.5), float)

def test_discount_mixed():
    assert calclulate_discount(150, 12.5) == 131.25
    assert round(calclulate_discount(99.99, 20), 2) == 79.99

def test_discount_invalid():
    with pytest.raises(ValueError):
        calclulate_discount(100, -1)
    with pytest.raises(ValueError):
        calclulate_discount(100, 110)
        