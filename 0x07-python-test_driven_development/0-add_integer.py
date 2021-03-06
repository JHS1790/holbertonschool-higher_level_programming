#!/usr/bin/python3
"""0. Integers addition"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
    a: first integer
    b: first integer

    Exceptions:
    TypeError: when a or b is not an int

    Returns:
    addition of a and b

    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return(a + b)
