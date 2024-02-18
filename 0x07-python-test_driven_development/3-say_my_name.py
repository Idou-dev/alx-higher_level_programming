#!/usr/bin/python3
"""Module prints my name"""


def say_my_name(first_name, last_name=""):
    """says my name

    Args:
        first_name: my first name string
        last_name: my last name string

    Raises:
        TypeError: if first name or last name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
