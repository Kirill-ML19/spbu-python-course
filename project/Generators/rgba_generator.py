from typing import Generator, Tuple


def rgba_generator() -> Generator[Tuple[int, int, int, int], None, None]:
    """
    Generator expression for creating a 4-dimensional set of RGBA vectors.
    Each color (R, G, B) takes values ​​between 0 and 255 inclusive.
    Alpha channel (A, transparency) takes only even values ​​between 0 and 100 inclusive.

    Return:
        Tuple[int, int, int, int]: Tuple (R, G, B, A).
    """
    return (
        (r, b, g, a)
        for r in range(256)
        for g in range(256)
        for b in range(256)
        for a in range(0, 101, 2)
    )


def get_rgba_element(index: int) -> Tuple[int, int, int, int]:
    """
    Returns the i-th element from the RGBA generator.

    Args:
        index (int): The index of the element (numbered from 0).

    Returns:
        Tuple[int, int, int, int]: The tuple (R, G, B, A) corresponding to the given index.
    """
    for i, value in enumerate(rgba_generator()):
        if i == index:
            return value
    raise IndexError("Index out of range")
