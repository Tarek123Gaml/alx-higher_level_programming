#!/usr/bin/python3
"""Module with BaseGeometry class"""


class BaseGeometry:
    """class whith method area"""

    def area(self):
        """method raise exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validate if a num is integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".formate(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".formate(name))
