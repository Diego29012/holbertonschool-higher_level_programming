#!/usr/bin/python3
"""added this line """


import json


class Base:
    """added this line """
    __nb_objects = 0

    def __init__(self, id=None):
        """added this line """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            """comments"""
            self.id = Base.__nb_objects
