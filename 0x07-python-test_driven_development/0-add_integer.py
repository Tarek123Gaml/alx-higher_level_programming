#!/usr/bin/python3
"""Module for add_intger method."""


def add_integer(a, b=98):
    """add tow intger.

    Args:
        a: the first intger.
        b: the second intger.

    Raises:
        TypeError: if a or b not int, float.

    Return:
        sum of tow intger
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
