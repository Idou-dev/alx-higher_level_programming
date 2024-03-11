#!/usr/bin/python3
"""Rectangle module"""
from base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self. __width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """getter for width: returns the rectangle width"""
        return self.__width

    def get_height(self):
        """getter for height: returns the rectangle height"""
        return self.__height

    def get_x(self):
        """returns the value of x"""
        return self.__x

    def get_y(self):
        """returns the value of y"""
        return self.__y

    def set_width(self, width):
        """setter methode for width"""
        self.__width = width

    def set_height(self, height):
        """setter methode for height"""
        self.__height = height

    def set_x(self, x):
        """setter methode for x"""
        self.__x = x

    def set_y(self, y):
        """setter methode for y"""
        self.__y = y
