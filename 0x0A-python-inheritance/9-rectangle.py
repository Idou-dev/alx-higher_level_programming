#!/usr/bin/python3
"""base goemetry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from basegeometry"""
    def __init__(self, width, height):
        """Instantiation..."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the erea of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation methode"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
