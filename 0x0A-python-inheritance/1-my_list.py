#!/usr/bin/python3
"""module with class Mylist"""


class MyList(list):
    """class with method print_sorted"""

    def print_sorted(self):
        """method that print sorted list"""

        print(sorted(list(self)))
