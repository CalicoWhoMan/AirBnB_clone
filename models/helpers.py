#!/usr/bin/python

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State

classDict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "City": City,
    "Review": Review,
    "Amenity": Amenity,
    "State": State
}
