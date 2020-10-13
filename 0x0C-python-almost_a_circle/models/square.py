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

    def update(self, *args, **kwargs):
        """update: updates the instance arguments
        Args:
        *args: voodoo black magic shit
        **kwargs: black voodoo magic shit on pervatin
        """
        if args:
            if len(args) >= 1:
                super(Rectangle, self).__init__(id=args[0])
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                super(Rectangle, self).__init__(kwargs['id'])
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    @property
    def size(self):
        """size: getter for size"""
        return super().width

    @size.setter
    def size(self, size):
        """size: setter for size"""
        Rectangle.width.fset(self, size)
        Rectangle.height.fset(self, size)
