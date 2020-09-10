#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            new_matrix[x] = list(map(lambda x: x**2, matrix[x]))
    return (new_matrix)
