#!/usr/bin/python3
import sys

if __name__ == "__main__":
    pass

argc = len(sys.argv) - 1
print("{:d} arguments:".format(argc))

for i in range(argc):
    print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
