#!/usr/bin/python3
"""append write module"""


def append_write(filename="", text=""):
    """
    append_write - appends a string at the end of a text file (UTF8)
                    and returns the number of characters added

    Args:
        filename: name of the file
        text: text added

    Return:
        number of chars added
    """
    with open(filename, 'a', encoding='UTF-8') as f:
        return (f.write(text))
