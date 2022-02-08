#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """City Class of BaseModel that contains thes attrs: state_id & mame"""
    state_id = ''
    name = ''
