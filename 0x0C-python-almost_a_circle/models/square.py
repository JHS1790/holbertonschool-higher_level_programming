#!/usr/bin/python3
"""square.py: file for the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square: class to build a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__: initializer method for square

        Args:
        size: size of the square
        x: x coordinate
        y: y coordinate
        id: identification number of instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """"__str__: string representation method
        Return:
        the string output
        """
        output = "[Square] ("
        output += str(self.id)
        output += ") "
        output += str(self.x)
        output += "/"
        output += str(self.y)
        output += " - "
        output += str(self.width)
        return output

    @property
    def size(self):
        """size: getter for size"""
        return super().width

    @size.setter
    def size(self, size):
        """size: setter for size"""
        self.__width = size
        self.__height = size
