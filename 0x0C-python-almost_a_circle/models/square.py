#!/usr/bin/python3
"""square method"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation for class square"""
        return (
                '[{}] ({}) {}/{} - {}'.format(
                    type(self).__name__, self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """the getter function for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter function for size"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """internat method that updates instance attribute */**args."""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if y is not None:
            self.y = y
        if x is not None:
            self.x = x

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """dictionary representation"""
        return (
                {"id": self.id, "size": self.size,
                    "x": self.x, "y": self.y})
