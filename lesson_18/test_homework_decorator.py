import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lesson_18')))

from homework_decorator import sample_function

@pytest.mark.parametrize("x, y, expected", [
    (10, 2, 5),
    (10, 0, None)
])
def test_sample_function(x, y, expected):
    assert sample_function(x, y) == expected