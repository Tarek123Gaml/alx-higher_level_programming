#!/usr/bin/python3
'''module for aquare class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''a Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''return human-readable'''
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''method of getter of size'''
        return self.width

    @size.setter
    def size(self, value):
        '''method of setter'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''method that update values'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        '''that returns the dictionary representation of a Square'''
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
