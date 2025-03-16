from typing import Callable , Any , Tuple

def curry_explicit(function: Callable , arity: int)->Callable:
    """
    Transforms a function into its curried version with the specified arity.

    A curried function allows partial application of arguments.
    When enough arguments (equal to the arity of the function) are provided, the function is executed. 
    Otherwise, it returns another function that takes the remaining arguments.

    Args:
        function (Callable): The function to be curried.
        arity (int): The number of arguments the function expects (its arity).
    
    Returns:
        Callable: A curried version of the input function.
    
    Raises:
        ValueError: 
                If arity is a negative number.
        TypeError: 
                If the function cannot be called or too many arguments are specified.
    """
    if not callable(function):
        raise TypeError("The provided function must be callable.")
    if arity<0:
        raise ValueError("Arity must be a non-negative integer.")
    if arity==0:
        if function.__code__.co_argcount > 0:
            raise ValueError("Arity is 0 , but the function expects arguments.")
        return function

    def inner_curry(args: Tuple[Any, ...])->Callable:
        if len(args)> arity:
            raise TypeError(f"Too many arguments. Expected {arity} , got {len(args)}")
        if len(args)==arity:
            return function(*args)
        return lambda arg: inner_curry(args+(arg, ))
    return inner_curry(())
