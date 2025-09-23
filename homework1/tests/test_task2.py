import sys
import os
import pytest

# Add the src folder to the path so import works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import task2
def test_int():
    assert task2.add_int(4, 5) == 9
    assert isinstance(task2.add_int(4, 5), int) 

def test_float():
    assert task2.mult_float(4.5, 5.5) == 24.75
    assert isinstance(task2.mult_float(4.5, 5.5), float)

def test_str():
    assert task2.check_str("Rayne") == "Hi, Rayne! How are you?"
    assert isinstance(task2.check_str("Rayne"), str)

def test_bool():
    assert task2.check_bool(4) is True
    assert task2.check_bool(5) is False
    assert isinstance(task2.check_bool(4), bool)