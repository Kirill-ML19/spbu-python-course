import pytest
from typing import Callable
from project.Decorators.curry_uncurry_func import curry_explicit, uncurry_explicit

# tests for curry_explicit


def test_curry_explicit_basic():
    """
    Check the base case of currying
    """

    def add(a, b, c):
        return a + b + c

    curried_add = curry_explicit(add, 3)
    assert curried_add(1)(2)(3) == 6


def test_curry_explicit_zero_arity():
    """
    Check the case when arity = 0
    """

    def zero_arg_func():
        return 42

    curried_func = curry_explicit(zero_arg_func, 0)
    assert curried_func() == 42


def test_curry_explicit_zero_arity_error():
    """
    Check for the case where arity = 0, but the function expects an argument.
    """

    def func_with_args(x):
        return x

    with pytest.raises(ValueError):
        curry_explicit(func_with_args, 0)


def test_curry_with_negative_arity():
    """
    Check for case when arity is negative
    """

    def func(a, b):
        return a + b

    with pytest.raises(ValueError):
        curry_explicit(func, -1)


def test_curry_explicit_too_many_args():
    """
    Check for the case when too many arguments are passed.
    """

    def func(a, b):
        return a + b

    curried_func = curry_explicit(func, 2)
    with pytest.raises(TypeError):
        curried_func(1)(2)(3)

def test_curry_explicit_multiple_args_error():
    """
    Check if multiple arguments passed simultaneously to a curried function cause an error.
    """
    def add(a,b):
        return a+b
    
    curried_add = curry_explicit(add,2)
    with pytest.raises(TypeError):
        curried_add(1,2)


def test_curry_explicit_built_in_function_sum():
    """
    Check currying of built-in function sum.
    """
    curried_sum = curry_explicit(sum,1)
    assert curried_sum([1,2,3])==6

def test_curry_explicit_built_in_function_len():
    """
    Check currying of built-in function len
    """
    curried_len = curry_explicit(len,1)
    assert curried_len([1,2,3,4])==4


# test for uncurry_explicit


def test_uncurry_explicit_basic():
    """
    Check the base case of uncurrying
    """

    def add(a, b, c):
        return a + b + c

    curried_add = curry_explicit(add, 3)
    uncurried_add = uncurry_explicit(curried_add, 3)
    assert uncurried_add(1, 2, 3) == 6


def test_uncurry_explicit_zero_arity():
    """
    Check the case when arity = 0
    """

    def zero_arg_func():
        return 42

    uncurried_func = uncurry_explicit(zero_arg_func, 0)
    assert uncurried_func() == 42


def test_uncurry_explicit_negative_arity():
    """
    Check for error when arity is negative.
    """

    def func(a, b):
        return a + b

    with pytest.raises(ValueError):
        uncurry_explicit(func, -1)


def test_uncurry_explicit_wrong_arg_count():
    """
    Check for error when number of arguments is incorrect.
    """

    def add(a, b, c):
        return a + b + c

    curried_add = curry_explicit(add, 3)
    uncurried_add = uncurry_explicit(curried_add, 3)
    with pytest.raises(ValueError):
        uncurried_add(1, 2)


def test_uncurry_not_fully_curried():
    """
    Check for an error if a function is not fully curried.
    """

    def add(a, b):
        return a + b

    with pytest.raises(TypeError):
        uncurry_explicit(add, 2)
