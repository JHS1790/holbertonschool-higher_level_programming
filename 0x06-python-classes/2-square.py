#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.ssize = size

    @property
    def ssize(self):
        return self.__size

    @ssize.setter
    def ssize(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
