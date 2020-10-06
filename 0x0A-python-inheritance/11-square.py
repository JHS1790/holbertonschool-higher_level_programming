#!/usr/bin/python3
"""file"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """class"""

    def __init__(self, size):
        """Mmethod"""
        BaseGeometry().integer_validator("size", size)
        super(Square, self).__init__(size, size)
        self.__size = size

    def area(self):
        """method"""
        return self.__size ** 2

    def __str__(self):
        """method"""
        retstr = "[Square] "
        retstr += str(self.__size)
        retstr += "/"
        retstr += str(self.__size)
        return retstr
