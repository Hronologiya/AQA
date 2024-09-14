import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lesson_18')))

from homework_iterator import get_reversed_list, get_even_numbers

@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([], [])
])
def test_get_reversed_list(data, expected):
    assert get_reversed_list(data) == expected

@pytest.mark.parametrize("n, expected", [
    (10, [0, 2, 4, 6, 8, 10]),
    (1, [0]),
    (0, [0])
])
def test_get_even_numbers(n, expected):
    assert get_even_numbers(n) == expected