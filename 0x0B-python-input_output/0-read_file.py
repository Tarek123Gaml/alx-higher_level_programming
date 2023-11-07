#!/usr/bin/python3

def read_file(filename=""):

    with open(filename) as f:
        read_d = f.read()

    print(read_d)
