#!/usr/bin/python3
"""my_list method"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """Public instance method that prints
        the list, but sorted (ascending sort)"""
        new_list = sorted(self)
        print(new_list)
