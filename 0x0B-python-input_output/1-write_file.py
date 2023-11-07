#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file (UTF8)
                    and returns the number of characters written

    Args:
        filename: name of the file
        text: text writed

    Return:
        number of characters
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        return (f.write(text))
