import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import task3

def test_num():
    assert task3.check_num(3) == "positive"
    assert task3.check_num(-3) == "negative"
    assert task3.check_num(0) == "zero"

def test_prime():
    assert task3.print_prime_nums() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_get_sum():
    assert task3.get_sum() == 101 * 100 // 2