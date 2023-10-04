#!/usr/bin/python3
for k in range(8):
    for j in range(k + 1, 10):
            print(f"{k}{j}", end=", ")
print(f"{k + 1}{j}")
