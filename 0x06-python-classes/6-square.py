#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        isit = True
        if type(value) is tuple:
            if isinstance(value[0], int):
                if isinstance(value[1], int):
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
        return self.size * self.size

    def my_print(self):
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
