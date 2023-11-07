#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """
    read_file - reads a text file (UTF8) and prints it to stdout

    Args:
        filename: name of the file
    """

    with open(filename, 'r', encoding='UTF-8') as f:
        read_d = f.read()

    print(read_d, end='')
