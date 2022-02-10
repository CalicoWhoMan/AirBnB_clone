#!/usr/bin/python
"""Documentation"""

import unittest
from models.review import Review

class Testreview(unittest.TestCase):
    def test__init__(self):
        test1 = Review()
        setattr(test1, "name", "test1")
        self.assertTrue(test1.name == "test1")
