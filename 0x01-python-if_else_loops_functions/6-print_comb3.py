#!/usr/bin/python3
for k in range(9):
    for j in range(k + 1, 10):
        if j != 9 & k !=  8:
            print(f"{k}{j}", end=", ")
        else:
            print(f"{k}{j}")
