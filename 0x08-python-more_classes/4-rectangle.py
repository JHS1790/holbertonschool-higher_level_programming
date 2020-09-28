#!/usr/bin/python3
"""This file is NEVER to be placed in a manila folder, on pain of termination"""


class Rectangle:
    """A class for the exposition and evangalization of the TRIANGLe, wait no,
    its a rectangle now, damn

    Attributes:
    width (int): the width of the rectangle
    height (int): the height of the rectangle
    """

    def __init__(self, width = 0, height = 0):
        """Initiate rectangular launch sequence, Vassily

        Args:
        width (int): expected width of square
        height (int): expected height of square
        """
        self.width = width
        self.height = height

    def __str__(self):
        """You know, strings are a lot like sand, they're annoying and they get
        everywhere"""
        string = ""
        for x in range(self.height):
            for y in range(self.width):
                string += '#'
            if x is not self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        string = "Rectangle("
        string += str(self.width)
        string += ", "
        string += str(self.height)
        string += ")"
        return string

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """the most secure perimeter south of Da Nang, if you don't count the
        rats"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width

        Args:
        value: int to make the width

        Raises:
        TypeError: if value is not an int
        ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height

        Args:
        value: int to make the height

        Raises:
        TypeError: if value is not an int
        ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
