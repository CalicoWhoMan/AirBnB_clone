#!/usr/bin/python3
"""this module holds the file_storage class"""


import json
import os


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
        self.__objects[str(type(obj)) + '.' + obj.id]\
            = obj.to_dict()


    def save(self):
        # first take all obj dictionaries from
        # __objects keys convert them to json strings
        # store those strings in a list and save each one
        # to the json file provided
        jsonList = []
        for key in self.__objects:
            jsonList.append(json.dumps(self.__objects[key]))
        with open(self.__filepath, 'w', encoding="utf-8") as jsonFile:
            for i in jsonList:
                json.dump(jsonList[i], jsonFile, ensure_ascii=False)

    @classmethod
    def reload(self):
        if os.path.isfile('file.json'):
            with open(self.__filepath, 'r', encoding="utf-8") as jsonFile:
                for line in jsonFile:
                    self.__objects.append(json.loads(line.strip))
