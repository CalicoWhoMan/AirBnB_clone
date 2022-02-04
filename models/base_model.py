#!/usr/bin/python3
"""this will be base of all classes"""


from queue import Empty
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """creates an instance"""
        if kwargs != {}:
            self.id = kwargs.get('id')
            self.created_at = \
                datetime.strptime(kwargs.get('created_at'),
                                  "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = \
                datetime.strptime(kwargs.get('updated_at'),
                                  "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns a string representation of an instance"""
        return \
            "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """changes the updated_at attr to current date and time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict of this instance"""
        rDict = self.__dict__
        rDict["__class__"] = type(self)
        rDict["created_at"] = self.created_at.isoformat()
        rDict["updated_at"] = self.updated_at.isoformat()
        return rDict
