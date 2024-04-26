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
