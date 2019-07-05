#!/usr/bin/python3
''' model review inherit from BaseModel '''

from models.base_model import BaseModel


class Review(BaseModel):
    ''' class Review to check the object '''
    place_id = ""
    user_id = ""
    text = ""
