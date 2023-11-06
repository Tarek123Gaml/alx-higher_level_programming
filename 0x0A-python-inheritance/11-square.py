#!/usr/bin/python3
"""module for square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """constructor"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

     def area(self):
        '''Method for area of square.'''
        return self.__size ** 2

    def __str__(self):
        '''Returns string representation of this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
