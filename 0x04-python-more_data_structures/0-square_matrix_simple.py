#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        sub_matrix = map(lambda n: n**2, i)
        new.append(list(sub_matrix))
    return new
