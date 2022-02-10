#!/usr/bin/python3
"""testing for AirBnB clone"""


import unittest
from models import base_model

# need to test all functions in class BaseClass init, __str__, save, to_dict

class TestBaseModel(unittest.TestCase):
    def test___init__(self):
        """tests the creation of an instance of basemodel class"""
        test1 = base_model()
        test2 = base_model()
        self.assertTrue(test1.id != test2.id)
        self.assertIsNotNone(test1.updated_at)
        self.assertIsNotNone(test1.created_at)
    #each time is set correctly (created and updated)

    def test___str__(self):
        """tests the output of printing an instance"""
        test1 = base_model()
        stringT = test1.__str__
        self.assertTrue(stringT, "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))
        test1.save()
        self.assertTrue(stringT != test1.__str__)

    def test_save(self):
        """test that the updated_on date has been changed correctly"""
        test1 = base_model()
        stringT = str(test1.updated_at)
        test1.save()
        self.assertTrue(stringT != test1.updated_at)
        # check around for time based testing tips
    def test_to_dict(self):
        """test that the correct dictionary output is given"""
        test1 = base_model()
        testDict = test1.__dict__
        testDict['__class__'] = type(test1)
        testDict["updated_at"] = test1.created_at
        testDict["created_at"] = test1.updated_at
