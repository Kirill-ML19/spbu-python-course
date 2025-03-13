from typing import List , Union 

def matrix_addition(mat1: List[List[Union[float,int]]], mat2: List[List[Union[float,int]]])->List[List[Union[float,int]]]:
    """
    Function adds matrices
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("")
    return [[mat1[i][j]+mat2[i][j]] for j in range(len(mat1[0])) for i in range(len(mat1))]

def matrix_multiplication(mat1: List[List[Union[float,int]]], mat2: List[List[Union[float,int]]])->List[List[Union[float,int]]]:
    """
    Function multiples matrix
    """
    if len(mat1[0]) != len(mat2):
        raise ValueError("")
    result=[[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j]+=mat1[i][k] * mat2[k][j]
    return result

def matrix_transpose(mat: List[List[Union[float,int]]])-> List[List[Union[float,int]]]:
    """
    Function that a transpose matrix
    """
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]