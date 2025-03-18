import pytest
import copy
from project.Decorators.smart_args import smart_args, Evaluated, Isolated

counter = 0


def generate_id():
    """
    Generates a unique ID (increments a global counter).

    Returns:
        int: The current counter value.
    """
    global counter
    counter += 1
    return counter


@smart_args
def example_func(a, b=Evaluated(generate_id), c=Isolated()):
    """
    Example function demonstrating smart_args behavior.

    Args:
        a (Any): A required argument.
        b (int, optional): A computed argument using Evaluated. Defaults to an incrementing counter.
        c (dict, optional): A deeply copied argument using Isolated. Must be explicitly provided.

    Returns:
        tuple: (a, computed b, copied c)
    """
    return a, b, c


def test_evaluated():
    """
    Tests that Evaluated computes a new value each time the function is called.
    """
    global counter
    counter = 0

    result1 = example_func(a=10, c={"key": "value"})
    result2 = example_func(a=20, c={"key": "another"})

    assert result1[1] == 1
    assert result2[1] == 2


def test_isolated():
    """
    Tests that Isolated arguments are deep copied.
    """
    config = {"key": "value"}
    result = example_func(a=10, c=config)

    assert result[2] == config
    assert result[2] is not config


def test_no_positional_args():
    """
    Tests that passing positional arguments raises an AssertionError.
    """
    with pytest.raises(AssertionError, match="Only keyword arguments are supported"):
        example_func(10, c={"key": "value"})


def test_missing_isolated():
    """
    Tests that Isolated arguments must be explicitly provided.
    """
    with pytest.raises(AssertionError, match="Argument 'c' must be provided"):
        example_func(a=10)


def test_combination_evaluated_isolated():
    """
    Tests that using both Evaluated and Isolated for the same argument raises a ValueError.
    """
    with pytest.raises(ValueError, match="cannot be both Isolated and Evaluated"):

        @smart_args
        def invalid_func(x=Evaluated(lambda: Isolated())):
            return x


def test_isolated_not_modified():
    """
    Tests in which isolated arguments remain unchanged even if they are changed inside the function.
    """

    def modify_dict(d):
        d["new_key"] = "new_value"

    config = {"key": "value"}

    result = example_func(a=10, c=config)
    modify_dict(result[2])

    new_result = example_func(a=20, c=config)
    assert "new_key" not in new_result[2], "Isolated argument was modified"
