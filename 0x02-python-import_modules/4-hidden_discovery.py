#!/usr/bin/python3
import  hidden_4
import sys

if __name__ != "__main__":
    exit()

for i in dir(hidden_4):
    if i[:2] != "__":
        print(i)
