#!/usr/bin/python
"""Documentation"""

import unittest
from models.place import Place

class Testplace(unittest.TestCase):
    def test__init__(self):
        test1 = Place()
        setattr(test1, "name", "test1")
        self.assertTrue(test1.name == "test1")