#!/usr/bin/python3
"""rectangle.py: file for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle: class for rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__: initializer method for Rectangle

        Args:
        width: width of the rectangle
        height: height of the rectangle
        x: x coordinate
        y: y coordinate
        id: instance id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    @property
    def width(self):
        """width: getter for __width

        Return:
        private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width: setter for __width

        Args:
        width: assignment value for __width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height: getter for __height

        Return:
        private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height: setter for __height

        Args:
        height: assignment value for __height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x: getter for __x

        Return:
        private instance attribute x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x: setter for __x

        Args:
        x: assignment value for __x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y: getter for __y

        Return:
        private instance attribute y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y: setter for __y

        Args:
        y: assignment value for __y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y