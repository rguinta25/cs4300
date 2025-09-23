import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task7 import calculate_grades

def test_grades():
    test = calculate_grades([1, 2, 3, 4, 5])
    assert test[0] == 3
    assert test[1] == 3

def test_empty():
    with pytest.raises(ValueError):
        calculate_grades([])