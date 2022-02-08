#!/usr/bin/python
"""Documentation"""

from models.user import User

class Testuser(unittest.TestCase):
    def test__init__(self):
        test1 = User()
        setattr(test1, name, "test1")
        self.assertTrue(test1.name == "test1")