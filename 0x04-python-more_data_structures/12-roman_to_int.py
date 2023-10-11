#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    ronum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        for i in roman_string:
            result += ronum[i]
        return result
