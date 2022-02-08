#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """The city class contains name and state_id"""
    state_id = ''
    name = ''
