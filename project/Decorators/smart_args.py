import copy
import functools
from inspect import signature


class Evaluated:
    """
    Wrapper class that represents an argument whose default value is computed at function call time.

    This is useful when the default value depends on external conditions (e.g., a changing counter or timestamp).

    Attributes:
        func (callable): A function that takes no arguments and returns a computed value.
    """

    def __init__(self, func):
        assert (
            callable(func) and func.__code__.co_argcount == 0
        ), "Evaluated expects a function with no arguments"
        self.func = func

    def evaluate(self):
        """
        Calls the stored function to compute the default value.

        Returns:
            Any: The computed value.
        """
        return self.func()


class Isolated:
    """
    Marker class used to indicate that an argument should always be deep copied before being used.

    This prevents unintended side effects when modifying mutable default values (e.g., lists or dictionaries).
    """

    pass


def smart_args(func):
    """
    Decorator that processes function arguments according to their default values.

    This decorator applies special handling for arguments with default values:
    - `Evaluated(func)`: The function `func` is called at each function invocation to compute the default value.
    - `Isolated()`: The argument must be explicitly passed, and it is deep copied to prevent mutations.

    Constraints:
    - Only keyword arguments are supported (no positional arguments).
    - An argument cannot use both `Evaluated` and `Isolated` simultaneously.
    - Arguments marked as `Isolated` must be explicitly provided when calling the function.

    Args:
        func (callable): The function to decorate.

    Returns:
        callable: The wrapped function with smart argument processing.

    Raises:
        AssertionError: If positional arguments are used when calling the function.
        ValueError: If an argument is both `Evaluated` and `Isolated`.
        AssertionError: If an argument marked as `Isolated` is not explicitly passed.
    """
    sig = signature(func)
    defaults = {
        name: param.default
        for name, param in sig.parameters.items()
        if param.default is not param.empty
    }

    # Validate that no argument is both Evaluated and Isolated
    for key, value in defaults.items():
        if isinstance(value, Evaluated) and isinstance(value.func(), Isolated):
            raise ValueError(f"Argument '{key}' cannot be both Isolated and Evaluated.")

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that processes argument values before calling the original function.

        Args:
            *args: Positional arguments (must be empty).
            **kwargs: Keyword arguments provided to the function.

        Returns:
            Any: The result of the original function.

        Raises:
            AssertionError: If positional arguments are used.
            AssertionError: If an `Isolated` argument is missing.
        """
        assert len(args) == 0, "Only keyword arguments are supported"

        # Populate new_kwargs with provided values or processed defaults
        new_kwargs = kwargs.copy()

        for key, value in defaults.items():
            if key not in new_kwargs:
                if isinstance(value, Evaluated):
                    new_kwargs[key] = value.evaluate()
                elif isinstance(value, Isolated):
                    raise AssertionError(f"Argument '{key}' must be provided")
                else:
                    new_kwargs[key] = value
            elif isinstance(value, Isolated):
                new_kwargs[key] = copy.deepcopy(new_kwargs[key])

        return func(**new_kwargs)

    return wrapper
