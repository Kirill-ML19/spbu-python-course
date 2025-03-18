from typing import Callable, Any, Tuple


def curry_explicit(function: Callable, arity: int) -> Callable:
    """
    Transforms a function into its curried version with the specified arity.

    A curried function allows partial application of arguments.
    When enough arguments (equal to the arity of the function) are provided, the function is executed.
    Otherwise, it returns another function that takes the remaining arguments.

    Args:
        function (Callable):
                        The function to be curried.
        arity (int):
                The number of arguments the function expects (its arity).

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
    if arity < 0:
        raise ValueError("Arity must be a non-negative integer.")
    if arity == 0:
        if function.__code__.co_argcount > 0:
            raise ValueError("Arity is 0 , but the function expects arguments.")
        return function

    def inner_curry(args: Tuple[Any, ...]) -> Callable:
        if len(args) > arity:
            raise TypeError(f"Too many arguments. Expected {arity} , got {len(args)}")
        if len(args) == arity:
            return function(*args)
        return lambda arg: inner_curry(args + (arg,))

    return inner_curry(())


def uncurry_explicit(function: Callable, arity: int) -> Callable:
    """
    Transforms a function into its curried version with a specified arity.

    A curried function allows partial application of arguments. When enough
    arguments (equal to the function's arity) are supplied, the function is
    executed. Otherwise, it returns another function that accepts the remaining arguments.

    Args:
        function (Callable):
                        The function to be curried.
        arity (int):
                The number of arguments the function expects (its arity).

    Returns:
        Callable: A curried version of the input function.

    Raises:
        ValueError:
                If the arity is a negative number.
        TypeError:
                If the function is not callable or too many arguments are supplied.
    """
    if not callable(function):
        raise TypeError("The provided function must be called.")
    if arity < 0:
        raise ValueError("Arity must be a positive integer.")
    if arity == 0:
        return lambda: function()

    temp_function = function
    for _ in range(arity):
        if not callable(temp_function):
            raise TypeError("The provided function is not fully curried.")
        try:
            temp_function = temp_function(0)
        except TypeError:
            raise TypeError("The provided function is not fully curried.")

    def inner_uncurry(*args: Any) -> Any:
        if len(args) != arity:
            raise ValueError(f"Excepted {arity} arguments, but got {len(args)}")
        result = function
        for arg in args:
            if not callable(result):
                raise TypeError("The provided function is not fully curried.")
            result = result(arg)
        return result

    return inner_uncurry
