import pytest 
from typing import Callable
from project.Decorators.curry_uncurry_func import curry_explicit , uncurry_exlicit

#tests for curry_explicit

def test_curry_explicit_basic():
    """
    Checking the base case of currying
    """
    def add(a,b,c):
        return a+b+c
    
    curried_add = curry_explicit(add, 3)
    assert curried_add(1)(2)(3)==6

def test_curry_explicit_zero_arity():
    """
    Checking the case when arity = 0
    """
    def zero_arg_func():
        return 42
    
    curried_func = curry_explicit(zero_arg_func , 0)
    assert curried_func() == 42

def test_curry_explicit_zero_arity_error():
    """
    Check for the case where arity = 0, but the function expects an argument.
    """
    def func_with_args(x):
        return x
    
    with pytest.raises(ValueError):
        curry_explicit(func_with_args , 0)

def test_curry_with_negative_arity():
    """
    Check for case when arity is negative
    """
    def func(a,b):
        return a+b
    
    with pytest.raises(ValueError):
        curry_explicit(func , -1)

def test_curry_explicit_too_many_args():
    """
    Check for the case when too many arguments are passed.
    """
    def func(a,b):
        return a+b
    
    curried_func = curry_explicit(func , 2)
    with pytest.raises(TypeError):
        curried_func(1)(2)(3)
