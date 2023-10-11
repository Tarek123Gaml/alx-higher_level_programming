#!/sur/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        sub_matrix = map(lambda n: n**2, i)
        new_matrix.append(list(sub_matrix))
    return new_matrix
