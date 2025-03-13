from matrix import matrix_addition, matrix_multiplication, matrix_transpose
from typing import List , Union

mat1: List[List[Union[float,int]]] = [[1, 2, 5], [2, 6, 9], [9, 5, 3]]
mat2: List[List[Union[float,int]]] = [[2, 8, 6], [5, 4, 9], [11, 2, 8]]
print(f"Adding matrix: {matrix_addition(mat1,mat2)}")
print(f"Multiplication matrix: {matrix_multiplication(mat1,mat2)}")
print(f"Transposing matrix: {matrix_transpose(mat2)}")
