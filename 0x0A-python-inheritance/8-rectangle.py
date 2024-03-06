#!/usr/bin/python3
"""base goemetry module"""


class BaseGeometry:
    """base goemetry class"""
    def area(self):
        """raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """class inherits from basegeometry"""
    def __init__(self, width, height):
        """Instantiation..."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
