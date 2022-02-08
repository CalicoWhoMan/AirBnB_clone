#!/usr/bin/python


from models.base_model import BaseModel

class User(BaseModel):
    """The user class which is strangely simple"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
