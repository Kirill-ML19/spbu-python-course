from vector import dot_product, vector_lenght, angle_betweeen_vectors
from typing import List

vec1: List[float] = [1.4, 2.8, 5.0]
vec2: List[float] = [5.2, 3.6, 7.2]

print(f"Dot product: {dot_product(vec1 , vec2)}")
print(f"Lenght vec1: {vector_lenght(vec1)}")
print(f"Lenght vec2: {vector_lenght(vec2)}")
print(f"Angle beetwen vec1 and vec2: {angle_betweeen_vectors(vec1 , vec2)}")
