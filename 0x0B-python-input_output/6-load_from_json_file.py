#!/usr/bin/python3
"""load_from_json_file module"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - creates an Object from a “JSON file”

    Args:
        filename: name of the file
    """
    with open(filename, 'r') as f:
        return (json.load(f))
