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
        """stores a dictionary of obj in __objects"""
        self.__objects[str(type(obj)) + '.' + obj.id]\
            = obj

    def save(self):
        # first take all obj dictionaries from
        # __objects keys convert them to json strings
        # store those strings in a list and save each one
        # to the json file provided
        jsonList = []
        wholeStr = ''
        for key in self.__objects:
            print(key)
            jsonList.append(json.dumps(self.__objects[key], default=str))
        with open(self.__filepath, 'w', encoding="utf-8") as jsonFile:
            for piece in jsonList:
                print(type(piece))
                wholeStr += piece
            json.dump(wholeStr, jsonFile, ensure_ascii=False)

    def reload(self):
        strList = []
        if os.path.isfile('file.json'):
            with open(self.__filepath, 'r', encoding="utf-8") as jsonFile:
                for line in jsonFile:
                    strList.append(json.loads(line.strip))
            for objJ in strList:
                self.new(objJ)
