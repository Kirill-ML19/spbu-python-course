import copy
import inspect
from functools import wraps


class Evaluated:
    """
    Class for calculating a default value when a function is called.

    Attributes:
        func (Callable):
            The function that will be called to calculate the default value.
    """

    def __init__(self, func):
        """
        Initializes the Evaluated object.

        Args:
            func (Callable):
                The function that will be called to evaluate the default value.

        """
        self.func = func


class Isolated:
    """
    Class for creating a deep copy of the passed argument.
    Used as a marker to indicate that the argument should be deep copied when passed to a function.
    """

    pass


def smart_args(func):
    """
    Decorator for handling function arguments.

    Supports:
        - Positional and named arguments.
        - Default values ​​of type `Evaluated` (evaluated at call time).
        - Default values ​​of type `Isolated` (a deep copy is created).

    Args:
        func (Callable):
            The function to apply the decorator to.

    Returns:
        Callable:
            The decorated function with support for argument handling.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Internal wrapper function for handling arguments.

        Args:
            *args: Positional arguments.
            **kwargs: Named arguments.

        Returns:
            Any:
                The result of executing the original function.
        """
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        for name, param in sig.parameters.items():
            if name in bound_args.arguments:
                if param.default is Isolated:
                    bound_args.arguments[name] = copy.deepcopy(
                        bound_args.arguments[name]
                    )
            elif isinstance(param.default, Evaluated):
                bound_args.arguments[name] = param.default.func()
        return func(*bound_args.args, **bound_args.kwargs)

    return wrapper
