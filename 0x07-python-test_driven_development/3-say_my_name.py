#!/usr/bin/python3
"""Module for say_my_name method"""


def say_my_name(first_name, last_name=""):
    """Print full name

    Ars:
        first_name: first name we print
        last_name: second name we print

    Raises:
        TypeError: if type of last or first name are not str
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
