#!/usr/bin/python3
"""Module for print_square method"""


def print_square(size):
    """Print square of size

    Ars:
        size: size of square printed.

    Raises:
        TypeError: if type size not intger or size less then 0.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print(('#' * size + "\n") * size, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
