#!/usr/bin/python3
"""base.py: file for Base class"""
import json


class Base():
    """
    Base class

    Args:
    __nb_objects: Number of objects created question mark?
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializer funtion

        Args:
        id: proposed id of new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or []:
            return "[]"
        return json.JSONEncoder().encode(list_dictionaries)
