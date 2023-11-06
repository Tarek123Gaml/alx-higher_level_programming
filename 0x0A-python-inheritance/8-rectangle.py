#!/usr/bin/python3
"""module for rectangle class"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass representing a rectangle.'''

    def _init__(self, width, height):
        """constructor"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
