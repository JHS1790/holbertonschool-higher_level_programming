#!/usr/bin/python3
class Square:
    """class to build a square

    Attributes:
        size (int): size of the square
        position (tuple): position of the square down and right
    """
    def __init__(self, size=0, position=(0,0)):
    """__init__ function for the Square class

    Args:
        size (int): size of the square, attribute assignment
        position (tuple): position of the square, attribute assignment
    """
        self.size = size
        self.position = position

    @property
    """int: size of the square"""
    def size(self):
        return self.__size

    @size.setter
    """
    Raises:
        TypeError: if value is not an int
        ValueError: if value is less than zero
    """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    """tuple: position of square right and down"""
    def position(self):
        return self.__position

    @position.setter
    """
    Raises:
        TypeError: if value is not a tuple of two positive integers
    """
    def position(self, value):
        isit = True
        if type(value) is tuple:
            if isinstance(value[0], int) and value[0] > 0:
                if isinstance(value[1], int) and value[1] > 0:
                    self.__position = value
                else:
                    isit = False
            else:
                isit = False
        else:
            isit = False
        if isit is False:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """method to find area of square"""
        return self.size * self.size

    def my_print(self):
        """method to print square"""
        for a in range(self.position[1]):
            print()
        for x in range(self.size):
            for b in range(self.position[0]):
                print(end=" ")
            for y in range(self.size):
                print("#", end="")
            print()
        if self.size == 0:
            print()
