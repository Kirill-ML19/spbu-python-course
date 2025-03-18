import pytest
from project.Decorators.cache import cached


def test_cached_decorator():
    """
    Checks that the cache saves the result and does not call the function again.
    """
    call_count = 0

    @cached()
    def add(a, b):
        nonlocal call_count
        call_count += 1
        return a + b

    assert add(1, 2) == 3
    assert call_count == 1 

    assert add(1, 2) == 3
    assert call_count == 1  


def test_cached_max_size():
    """
    Tests the operation of a cache with a limited size.
    """
    call_count = 0

    @cached(max_size=2)
    def add(a, b):
        nonlocal call_count
        call_count += 1
        return a + b

    assert add(1, 2) == 3
    assert call_count == 1

    assert add(2, 3) == 5
    assert call_count == 2

    assert add(3, 4) == 7
    assert call_count == 3  

    assert add(1, 2) == 3
    assert call_count == 4  


def test_cached_with_kwargs():
    """
    Checks that the cache works with named arguments.
    """
    call_count = 0

    @cached()
    def multiply(a, b):
        nonlocal call_count
        call_count += 1
        return a * b

    assert multiply(a=2, b=3) == 6
    assert call_count == 1

    assert multiply(a=2, b=3) == 6  
    assert call_count == 1


def test_cached_with_different_types():
    """
    Checks that the cache distinguishes between arguments of different types.
    """
    call_count = 0

    @cached()
    def concat(a, b):
        nonlocal call_count
        call_count += 1
        return str(a) + str(b)

    assert concat(1, 2) == "12"
    assert concat("a", "b") == "ab"
    assert concat(1.5, 2.5) == "1.52.5"
    assert call_count == 3  

    assert concat(1, 2) == "12"
    assert concat("a", "b") == "ab"
    assert concat(1.5, 2.5) == "1.52.5"
    assert call_count == 3  


def test_cached_no_max_size():
    """
    Checks cache without size limitation.
    """
    call_count = 0

    @cached(max_size=None)
    def subtract(a, b):
        nonlocal call_count
        call_count += 1
        return a - b

    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(7, 2) == 5
    assert call_count == 3  

    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(7, 2) == 5
    assert call_count == 3  


def test_cached_no_args():
    """
    Checks the cache for functions with no arguments.
    """
    call_count = 0

    @cached()
    def get_value():
        nonlocal call_count
        call_count += 1
        return 42

    assert get_value() == 42
    assert call_count == 1

    assert get_value() == 42  
    assert call_count == 1  
