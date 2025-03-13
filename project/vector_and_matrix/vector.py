import math
from typing import List, Union


def dot_product(
    vec1: List[Union[float, int]], vec2: List[Union[float, int]]
) -> Union[float, int]:
    """
    Function calculates the dot product
    """
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be the same length")
    return sum(x * y for x, y in zip(vec1, vec2))


def vector_lenght(vec: List[Union[float, int]]) -> float:
    """
    Function caclulates the length of a vector
    """
    return math.sqrt(sum(x**2 for x in vec))


def angle_betweeen_vectors(
    vec1: List[Union[float, int]], vec2: List[Union[float, int]]
) -> float:
    """
    Function calculates the angle between vectors
    """
    dot = dot_product(vec1, vec2)
    len1 = vector_lenght(vec1)
    len2 = vector_lenght(vec2)
    return math.acos(dot / (len1 * len2))
