#!/usr/bin/python3
"""inherits from list"""


class MyList(list):
    """inherits from list"""
    def __init__(self):
        """__init__ class"""
        super().__init__()

    def print_sorted(self):
        """method for printing sorted list"""
        print(sorted(self))
