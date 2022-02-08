#!/usr/bin/python


from models.base_model import BaseModel

class User(BaseModel):
    """City Class of BaseModel that contains thes attrs:
    email, password, first&last names"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
