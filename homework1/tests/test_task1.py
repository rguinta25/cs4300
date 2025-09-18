import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task1 import main  

def test_hello(capsys):
    main()
    output = capsys.readouterr()
    assert output.out == "Hello, World!\n"
