#!/usr/bin/python3
"""creates a Rectangle class"""


class Rectangle:
    """Rectagle class"""

    number_of_instances = 0
    """int: the number of instances"""

    print_symbol = "#"
    """type: print symbol"""

    def __init__(self, width=0, height=0):
        """__init__ methode

        Args:
            width: the rectangle width
            height: the height width
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property of rectangle width

        Raises:
            TypeError: if width is not an int
            ValueError: if width is < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property of rectangle height

        Raises:
            TypeError: if height is not an int
            ValueError: if height < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle erea

        Return:
            the rectangle erea
        """
        return self.__height * self.__width

    def perimeter(self):
        """returns a rectangle perimeter

        Return:
            the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """returns printable string"""
        string = ""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """return a string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
