#!/usr/bin/python3
"""rectangle module"""


class Rectangle:
    """defines a Rectangle class"""
    def __init__(self, width=0, height=0):
        """Instantiation methode"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the Private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the instance width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the Private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the erea of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """string representation"""
        s = ""
        if self.__width != 0 and self.__height != 0:
            s += "\n".join("#" * self.__width for i in range(self.__height))
        return s
