#!/usr/bin/python3
"""save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - writes an Object to a text file

    Args:
        my_obj: object to file
        fileame: name of the file

    Return:
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
