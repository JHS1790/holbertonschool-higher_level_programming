#!/usr/bin/python3
"""file"""


class Student():
    """class"""

    def __init__(self, first_name, last_name, age):
        """method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method"""
        if attrs == None:
            return self.__dict__
        if type(attrs) is list:
            for i in range(len(attrs)):
                if type(attrs[i]) is not str:
                    return self.__dict__
        else:
            return self.__dict__
        NewDict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                NewDict[key] = value
        return NewDict
