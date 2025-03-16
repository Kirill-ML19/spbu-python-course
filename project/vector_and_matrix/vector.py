import math
from typing import List


def dot_product(vec1 : List[float] ,vec2: List[float] ):
    
    """
    Calculates the dot product of two vectors.

    Args:
        vec1 (List[float]): The first vector.
        vec2 (List[float]): The second vector.

    Returns:
        float: The dot product of the two vectors.

    Raises:
        ValueError: If the vectors are not of the same length.
    """

    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be the same length")
    return sum(x * y for x, y in zip(vec1, vec2))


def vector_length(vec: List[float]) -> float:
    
    """
    Calculates the length (magnitude) of a vector.

    Args:
        vec (List[float]): The vector.

    Returns:
        float: The length of the vector.
    """

    return math.sqrt(sum(x**2 for x in vec))


def angle_between_vectors(vec1: List[float] , vec2: List[float]) -> float:
    
    """
    Calculates the angle between two vectors in radians.

    Args:
        vec1 (List[float]): The first vector.
        vec2 (List[float]): The second vector.

    Returns:
        float: The angle between the vectors in radians.

    Raises:
        ValueError: If either vector has zero length.
    """

    dot = dot_product(vec1, vec2)
    len1 = vector_length(vec1)
    len2 = vector_length(vec2)
    if len1==0 or len2==0:
        raise ValueError("Vectors must not have zero length")
    return math.acos(dot / (len1 * len2))
