#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for i in my_string:
        if i is not 'C' and i is not 'c':
            new += i
    return new
