#!/usr/bin/python3
"""inherits from list"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """method for printing sorted list"""
        print(sorted(self))
