#!/usr/bin/python
"""Documentation"""

import unittest
from models.amenity import Amenity

class Testamenity(unittest.TestCase):
    def test__init__(self):
        test1 = Amenity()
        setattr(test1, "name", "test1")
        self.assertTrue(test1.name == "test1")
