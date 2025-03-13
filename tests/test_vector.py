import math
import pytest
from project.vector_and_matrix.vector import (
    dot_product,
    vector_lenght,
    angle_betweeen_vectors,
)


def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert dot_product([1.5, 2.5], [3.0, 4.0]) == 14.5
    assert dot_product([0, 0], [0, 0]) == 0
    with pytest.raises(ValueError):
        dot_product([1, 2], [2, 3, 6])


def test_vector_lenght():
    assert vector_lenght([3, 4]) == 5.0
    assert vector_lenght([0, 0, 0]) == 0.0
    assert math.isclose(vector_lenght([1.0, 1.0]), math.sqrt(2))


def test_angle_between_vectors():
    vec1 = [1, 0]
    vec2 = [0, 1]
    assert math.isclose(angle_betweeen_vectors(vec1, vec2), math.pi / 2)

    vec1 = [1, 0]
    vec2 = [2, 0]
    assert math.isclose(angle_betweeen_vectors(vec1, vec2), 0.0)

    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    dot = dot_product(vec1, vec2)
    len1 = vector_lenght(vec1)
    len2 = vector_lenght(vec2)
    angle = math.acos(dot / (len1 * len2))
    assert math.isclose(angle_betweeen_vectors(vec1, vec2), angle)

    with pytest.raises(ValueError):
        angle_betweeen_vectors([1, 2], [2, 4, 7])
