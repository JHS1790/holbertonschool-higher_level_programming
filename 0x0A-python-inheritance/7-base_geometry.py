#!/usr/bin/python3
"""file"""


class BaseGeometry():
    """class"""

    def area(self):
        """method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
