import sys
import os
import pytest

# Add the src folder to the path so import works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task1 import hello_world  

def test_hello(capsys):
    assert hello_world() == "Hello, World!"
