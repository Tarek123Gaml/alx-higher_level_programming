#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    re = True

    try:
        print("{:d}".format(value))
    except Exception as r:
        print("Exception:", r, file=sys.stderr)
        re = False
    return re
