#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if chr(c) is not "q" and chr(c) is not "e":
        print("{:s}".format(chr(c)), end="")
