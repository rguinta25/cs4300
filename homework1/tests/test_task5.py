import sys
import os
import pytest

# Add the src folder to the path so import works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import task5


def test_books():
    assert task5.fav_books() == ['A Tale of Two Cities by Charles Dickens', 
    'The Alchemest by Paulo Coelho', 
    'Harry Potter by J. K. Rowling']

def test_student():
    assert task5.student(2) == "Rayne Guinta"
    assert task5.student(5) == "student doesn't exist"
