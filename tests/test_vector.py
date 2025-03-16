import math
import pytest
from project.vector_and_matrix.vector import (
    dot_product,
    vector_length,
    angle_between_vectors,
)


def test_dot_product():
    """
    Testing the dot_product function.
    Checks the correctness of the calculation of the scalar product.
    """
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32

    assert dot_product([1.5, 2.5], [3.0, 4.0]) == 14.5

    assert dot_product([0, 0], [0, 0]) == 0

    with pytest.raises(ValueError):
        dot_product([1, 2], [2, 3, 6])


def test_vector_length():
    """
    Testing the vector_length function.
    Checks the correctness of the vector length calculation.
    """
    assert vector_length([3, 4]) == 5.0

    assert vector_length([0, 0, 0]) == 0.0

    assert math.isclose(vector_length([1.0, 1.0]), math.sqrt(2))


@pytest.mark.parametrize(
    "vec1, vec2, expected_angle",
    [
        ([1, 0], [0, 1], math.pi / 2),
        ([1, 0], [2, 0], 0.0),
        ([1, 2, 3], [4, 5, 6], math.acos(32 / (math.sqrt(14) * math.sqrt(77)))),
    ],
)
def test_angle_between_vectors(vec1, vec2, expected_angle):
    """
    Testing the angle_between_vectors function.
    Checks whether the angle between vectors is calculated correctly.
    """
    assert math.isclose(angle_between_vectors(vec1, vec2), expected_angle)


def test_angle_between_vectors_raises_value_error():
    """
    Testing the angle_between_vectors function for throwing an exception.
    Checks that the function raises ValueError for different vector lengths.
    """
    with pytest.raises(ValueError):
        angle_between_vectors([1, 2], [2, 4, 7])
