import pytest
from homework_generator import even_numbers, fibonacci


def test_even_numbers():  # Test for the even number generator.
    result = list(even_numbers(10))
    assert result == [0, 2, 4, 6, 8, 10]


def test_fibonacci():   # Test for Fibonacci Sequence Generator.
    result = list(fibonacci(10))
    assert result == [0, 1, 1, 2, 3, 5, 8]


if __name__ == "__main__":
    pytest.main()
