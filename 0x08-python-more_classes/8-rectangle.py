#!/usr/bin/python3
"""rectangle module"""


class Rectangle:
    """defines a Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation methode"""
        Rectangle.number_of_instances += 1
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
        if self.__width == 0 and self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.width +
                "\n") * self.height)[:-1]

    def __repr__(self):
        """returns string representation"""
        return ("Rectangle)" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """prints the message Bye rectangle...
        when an instance rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        return rect_2
