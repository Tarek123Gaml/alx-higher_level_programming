#!/usr/bin/python3
def no_c(my_string):
    l = 0
    for i in my_string:
        if i is in 'cC':
            my_string[l] = ''
        l += 1
    return my_string