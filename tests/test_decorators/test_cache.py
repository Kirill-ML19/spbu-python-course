import pytest
from project.Decorators.cache import cached


def test_cached_decorator():
    @cached()
    def add(a, b):
        return a + b

    assert add(1, 2) == 3

    assert add(1, 2) == 3


def test_cached_max_size():
    @cached(max_size=2)
    def add(a, b):
        return a + b

    assert add(1, 2) == 3
    assert add(2, 3) == 5

    assert add(3, 4) == 7

    assert add(1, 2) == 3


def test_cached_with_kwargs():
    @cached()
    def multiply(a, b):
        return a * b

    assert multiply(a=2, b=3) == 6

    assert multiply(a=2, b=3) == 6


def test_cached_with_different_types():
    @cached()
    def concat(a, b):
        return str(a) + str(b)

    assert concat(1, 2) == "12"
    assert concat("a", "b") == "ab"
    assert concat(1.5, 2.5) == "1.52.5"


def test_cached_no_max_size():
    @cached(max_size=None)
    def subtract(a, b):
        return a - b

    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(7, 2) == 5

    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(7, 2) == 5


def test_cached_no_args():
    @cached()
    def get_value():
        return 42

    assert get_value() == 42

    assert get_value() == 42
