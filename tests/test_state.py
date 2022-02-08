#!/usr/bin/python
"""Documentation"""

from models.state import State

class Teststate(unittest.TestCase):
    def test__init__(self):
        test1 = State()
        setattr(test1, name, "test1")
        self.assertTrue(test1.name == "test1")