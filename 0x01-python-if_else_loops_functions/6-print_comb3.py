#!/usr/bin/python3
for k in range(8):
    for j in range(k + 1, 10):
        print("{:d}{:d}".format(k, j), end=", ")
print("{:d}{:d}".format(k + 1, j))
