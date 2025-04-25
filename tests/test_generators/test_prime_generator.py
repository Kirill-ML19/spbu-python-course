import pytest
from project.Generators.generator_prime_number import get_prime


@pytest.mark.parametrize(
    "index, expected",
    [
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 7),
        (5, 11),
        (10, 29),
    ],
)
def test_get_prime(index, expected):
    """
    Tests that get_prime returns the correct k-th prime number.
    """
    assert get_prime(index) == expected


def test_get_prime_invalid_index():
    """
    Tests that get_prime raises a ValueError for invalid indices.
    """
    with pytest.raises(ValueError, match="Index must be greater than or equal to 1"):
        get_prime(0)
    with pytest.raises(ValueError, match="Index must be greater than or equal to 1"):
        get_prime(-1)
