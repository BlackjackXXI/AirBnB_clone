#!/usr/bin/python3
""" Define city subclass that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Define city subclass that inherits from BaseModel """
    state_id = ""
    name = ""
