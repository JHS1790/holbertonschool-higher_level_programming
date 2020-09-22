#!/usr/bin/python3
"""file for class square"""
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
        self.__size = size
