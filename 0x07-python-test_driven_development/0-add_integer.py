#!/usr/bin/python3
"""add integer module"""


def add_integer(a, b=98):
    """
    adds two integers
    Args:
        a: first integer
        b: second integer
    Raises:
        TypeError: if a or b are not float or int
    Return:
        the addition of a and b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.tesfile("tests/0-add_integer.txt")
