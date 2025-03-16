import pytest
from project.vector_and_matrix.matrix import (
    matrix_addition,
    matrix_multiplication,
    matrix_transpose,
)


@pytest.mark.parametrize(
    "mat1, mat2, expected",
    [
        ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[6, 8], [10, 12]]),
        ([[1.5, 2.5], [3.0, 4.0]], [[0.5, 1.5], [2.0, 3.0]], [[2.0, 4.0], [5.0, 7.0]]),
    ],
)
def test_matrix_addition(mat1, mat2, expected):
    """
    Testing the matrix_addition function.
    Checks the correctness of matrix addition.
    """
    assert matrix_addition(mat1, mat2) == expected


def test_matrix_addition_raises_value_error():
    """
    Testing the matrix_addition function for throwing an exception.
    Checks that the function throws ValueError for different matrix sizes.
    """
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError):
        matrix_addition(mat1, mat2)


@pytest.mark.parametrize(
    "mat1, mat2, expected",
    [
        ([[1, 2], [3, 4]], [[2, 0], [1, 2]], [[4, 4], [10, 8]]),
        ([[1.5, 2.5], [3.0, 4.0]], [[0.5, 1.5], [2.0, 3.0]], [[5.75, 9.75], [9.5, 16.5]]),
    ],
)
def test_matrix_multiplication(mat1, mat2, expected):
    """
    Testing the matrix_multiplication function.
    Checks the correctness of matrix multiplication.
    """
    assert matrix_multiplication(mat1, mat2) == expected


def test_matrix_multiplication_raises_value_error():
    """
    Tests the matrix_multiplication function for throwing an exception.
    Checks that the function raises ValueError when the matrix sizes are incompatible.
    """
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValueError):
        matrix_multiplication(mat1, mat2)


@pytest.mark.parametrize(
    "mat, expected",
    [
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
    ],
)
def test_matrix_transpose(mat, expected):
    """
    Testing the matrix_transpose function.
    Checks the correctness of matrix transposition.
    """
    assert matrix_transpose(mat) == expected


def test_matrix_transpose_raises_value_error():
    """
    Testing the matrix_transpose function for throwing an exception.
    Checks that the function raises ValueError when the matrix is ​​empty.
    """
    with pytest.raises(ValueError):
        matrix_transpose([])