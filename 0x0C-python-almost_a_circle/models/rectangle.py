#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """"constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """width setter"""
        self.validate_integer("width", width, False)
        self.__width = width

    @height.setter
    def height(self, height):
        """height setter"""
        self.validate_integer("height", height, False)
        self.__height = height

    @x.setter
    def x(self, x):
        """x setter"""
        self.validate_integer("x", x)
        self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        self.validate_integer("y", y)
        self.__y = y

    def validate_integer(self, name, value, eq=True):
        """validates integer methode"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0")

    def area(self):
        """returns the rectangle erea"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{}] ({}) {}/{} - {}/{}".\
                format(type(self).__name__, self.id, self.__x, self.__y, self.__width,
                        self.__height)
