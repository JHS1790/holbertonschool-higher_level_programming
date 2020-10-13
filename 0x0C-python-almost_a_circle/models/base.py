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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string: turns a list of class dicts into a json string

        Args:
        list_dictionaries: the dict representations of various instances in
        a list

        Return:
        the requisite json string
        """
        if list_dictionaries is None or []:
            return "[]"
        return json.JSONEncoder().encode(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file: saves a json string to a file

        Args:
        list_objs: list of instances in dict format
        """
        debug_check = True
        if list_objs is None:
            list_objs = []
        list_dictionaries = [
            instance.to_dictionary() for instance in list_objs
        ]
        WorkingList = cls.to_json_string(list_dictionaries)
        if list_objs[0].__class__.__name__ is 'Rectangle':
            with open("./Rectangle.json", mode='w') as WorkingFile:
                WorkingFile.write(WorkingList)
            debug_check = False
        if list_objs[0].__class__.__name__ is 'Square':
            with open("./Square.json", mode='w') as WorkingFile:
                WorkingFile.write(WorkingList)
            debug_check = False
        if debug_check:
            print("fix your shit")
