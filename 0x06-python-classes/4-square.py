#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """__init__ class

        Args:
            size: length of the square
        """
        self.__size = size

    @property
    def size(self):
        """property to retrieve the size attribute

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2
