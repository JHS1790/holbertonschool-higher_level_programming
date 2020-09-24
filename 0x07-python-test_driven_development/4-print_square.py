#!/usr/bin/python3
"""3. Print square"""
def print_square(size):
    """prints a square

    Args:
    size: integer or float indicating final size of square

    Exceptions:
    TypeError: if size is not an integer or float, or if a negative float
    ValueError: if size is negative

    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
