#!/usr/bin/python3
"""File for class Square"""


class Square:
    """class to build a square

    Attributes:
    size (int): size of the square
    position (tuple): position of the square down and right
    """
    def __init__(self, size=0):
        """__init__ function for the Square class

        Args:
        size (int): size of the square, attribute assignment
        position (tuple): position of the square, attribute assignment
        """
        self.size = size

    @property
    def size(self):
        """int: size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Raises:
        TypeError: if value is not an int
        ValueError: if value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method to find area of square"""
        return self.size * self.size

    def my_print(self):
        """method to print square"""
        for x in range(self.size):
            for y in range(self.size):
                print("#", end="")
            print()
        if self.size == 0:
            print()
