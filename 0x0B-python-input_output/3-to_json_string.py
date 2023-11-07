#!/usr/bin/python3
"""to json string module"""
import json


def to_json_string(my_obj):
    """
    to_json_string -  returns the JSON representation of an object (string)

    Args:
        my_obj - list of string return
    """
    return (json.dumps(my_obj))
