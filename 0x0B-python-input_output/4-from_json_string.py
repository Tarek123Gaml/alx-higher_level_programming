#!/usr/bin/python3
"""from_json_string module"""
import json


def from_json_string(my_str):
    """
    from_json_string - returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: string we convert

    Return:
        python data structure
    """
    return (json.loads(my_str))
