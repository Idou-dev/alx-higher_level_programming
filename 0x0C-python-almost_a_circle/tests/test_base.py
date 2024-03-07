#!/usr/bin/python3
"""module for Base unit tests"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests the Base class"""

    def setup(self):
        """imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass
