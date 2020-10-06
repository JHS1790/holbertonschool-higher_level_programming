#!/usr/bin/python3
"""file"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
bg = BaseGeometry()


class Rectangle(BaseGeometry):
    """class"""

    def __init__(self, width, height):
        """method"""
        bg.integer_validator("width", width)
        bg.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method"""
        return self.__width * self.__height

    def __str__(self):
        """method"""
        retstr = "[Rectangle] "
        retstr += str(self.__width)
        retstr += "/"
        retstr += str(self.__height)
        return retstr
