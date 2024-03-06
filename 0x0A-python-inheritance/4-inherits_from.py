#!/usr/bin/python3
"""for inherits from method"""


def inherits_from(obj, a_class):
    """determines if an object is a true subclass"""
    return isinstance(obj, a_class) and type(obj) is not a_class
