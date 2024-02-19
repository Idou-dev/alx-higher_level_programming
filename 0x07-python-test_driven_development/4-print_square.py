#!/usr/bin/python3
"""Module prints a square with #"""


def print_square(size):
    """prints a square with #

    Args:
        size: the size of the square

    Raises:
        TypeError: if size is not an int
        ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/4-print_square.txt')
