from typing import List, Union


def matrix_addition(mat1: List[List[float]] ,mat2: List[List[float]])->List[List[float]]:
    """
    Adds two matrices element-wise.

    Args:
        mat1 (List[List[float]]): The first matrix.
        mat2 (List[List[float]]): The second matrix.

    Returns:
        List[List[float]]: The resulting matrix after addition.

    Raises:
        ValueError: If the matrices are not of the same size.
    """
    if not mat1 or not mat2:
        raise ValueError("Matrices must not be empty")
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("The matrices must be the same size")
    return [
        [mat1[i][j]+mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))
    ]

def matrix_multiplication(mat1: List[List[float]] , mat2: List[List[float]])->List[List[float]]:
    """
    Multiplies two matrices.

    Args:
        mat1 (List[List[float]]): The first matrix.
        mat2 (List[List[float]]): The second matrix.

    Returns:
        List[List[float]]: The resulting matrix after multiplication.

    Raises:
        ValueError: If the number of columns in the first matrix does not match
                   the number of rows in the second matrix.
    """
    if not mat1 or not mat2:
        raise ValueError("Matrices must not be empty")
    if len(mat1[0]) != len(mat2):
        raise ValueError("The number of columns in the first matrix and rows in the second matrix must be the same")
    result: List[List[float]] = [
        [0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))
    ]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


def matrix_transpose(mat: List[List[float]])->List[List[float]]:
    """
    Transposes a matrix (swaps rows and columns).

    Args:
        mat (List[List[float]]]): The matrix to transpose.

    Returns:
        List[List[float]]]: The transposed matrix.

    Raises:
        ValueError: If the matrix is empty.
    """
    if not mat:
        raise ValueError("Matrix must not be empty")
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
