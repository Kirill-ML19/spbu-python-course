import pytest
from .. import (
    matrix_addition,
    matrix_multiplication,
    matrix_transpose,
)


def test_matrix_addition():

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert matrix_addition(mat1, mat2) == expected

    mat1 = [[1.5, 2.5], [3.0, 4.0]]
    mat2 = [[0.5, 1.5], [2.0, 3.0]]
    expected = [[2.0, 4.0], [5.0, 7.0]]
    assert matrix_addition(mat1, mat2) == expected

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError):
        matrix_addition(mat1, mat2)


def test_matrix_multiplication():

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[2, 0], [1, 2]]
    expected = [[4, 4], [10, 8]]
    assert matrix_multiplication(mat1, mat2) == expected

    mat1 = [[1.5, 2.5], [3.0, 4.0]]
    mat2 = [[0.5, 1.5], [2.0, 3.0]]
    expected = [[5.75, 9.75], [9.5, 16.5]]
    assert matrix_multiplication(mat1, mat2) == expected

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValueError):
        matrix_multiplication(mat1, mat2)


def test_matrix_transpose():

    mat = [[1, 2], [3, 4]]
    expected = [[1, 3], [2, 4]]
    assert matrix_transpose(mat) == expected

    mat = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert matrix_transpose(mat) == expected

    mat = [[1, 2, 3]]
    expected = [[1], [2], [3]]
    assert matrix_transpose(mat) == expected

    mat = [[1], [2], [3]]
    expected = [[1, 2, 3]]
    assert matrix_transpose(mat) == expected
