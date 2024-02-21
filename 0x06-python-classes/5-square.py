#!/usr/bin/python3
"""defines a square"""


class Square:
    """defines and prints a square"""

    def __init__(self, size=0):
        """__init__ class

        Args:
            size: the size of square
        """
        self.__size = size

    @property
    def size(self):
        """property for the length of square

        Raises:
            TypeError: if size is not int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size == value

    def area(self):
        """area of the square

        Returns:
            the size of the square
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="\n" if j is self.__size - 1 and i != j else "")
        print()
