#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda(map(lambda x: x ** 2, x[:])),matrix))
