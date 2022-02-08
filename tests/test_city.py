#!/usr/bin/python
"""Documentation"""

from models.city import City

class Testcity(unittest.TestCase):
    def test__init__(self):
        test1 = City()
        setattr(test1, name, "test1")
        self.assertTrue(test1.name == "test1")