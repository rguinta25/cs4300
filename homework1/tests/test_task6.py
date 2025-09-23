import sys
import os
import pytest

# Add the src folder to the path so import works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task6 import count_words

def test_word_count():
    # 127 words in file
    assert count_words("task6_read_me.txt") == 127

def test_word_count_error():
    # Test if file is empty
    with pytest.raises(FileNotFoundError):
        count_words("blah.txt")