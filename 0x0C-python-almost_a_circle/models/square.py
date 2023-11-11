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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
