#!/usr/bin/python3
"""class method"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass square"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method for area square"""
        return self.__size * self.__size

    def __str__(self):
        """string representation"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
