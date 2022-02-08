#!/usr/bin/python3
"""this module holds the file_storage class"""


import json
import os
from json import JSONEncoder
import models


class BaseClassEncoder(JSONEncoder):
    """Encodes input for a JSONdump"""
    def default(self, o):
        return o.to_dict()


class FileStorage:
    """contains methods and attributes for storing object
    in files"""

    def __init__(self, filepath='file.json', objects={}):
        """creates a file_storage object"""
        self.__filepath = filepath
        self.__objects = objects

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """stores an obj in __objects"""
        self.__objects[(str(obj.__class__.__name__)) + '.' + obj.id] = obj

    def save(self):
        # first take all obj dictionaries from
        # __objects keys convert them to json strings
        # store those strings in a list and save each one
        # to the json file provided
        with open(self.__filepath, 'w', encoding="utf-8") as jsonFile:
            for key in self.__objects:
                instObj = self.__objects[key]
                jsonStr = json.dumps(instObj, cls=BaseClassEncoder)
                jsonFile.write(jsonStr + '\n')

    def reload(self):
        strList = []
        if os.path.isfile('file.json'):
            with open(self.__filepath, 'r', encoding="utf-8") as jsonFile:
                for line in jsonFile:
                    strList.append(json.loads(line))
            for objJ in strList:
                from models.helpers import classDict
                for key, value in classDict.items():
                    if objJ['__class__'] == key:
                        newObj = value(kwargs=objJ)
                        self.new(newObj)
