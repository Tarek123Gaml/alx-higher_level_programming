#!/usr/bin/python3
for i in range(100):
    print(f"{i // 10}{i % 10}", end="")
    if i != 99:
        print(", ", end="")

