#!/usr/bin/python3
"""base geometry methode"""


class BaseGeometry:
    """BaseGeomety class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/7-base_geometry.txt')
