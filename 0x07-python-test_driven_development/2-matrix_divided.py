#!/usr/bin/python3
"""1. Divide a matrix """


def matrix_divided(matrix, div):
    """Divides a Matrix

    Args:
    matrix: A list of lists of ints or floats
    div: a non zero int or float

    Exceptions:
    TypeError: if the matrix and/or div is not as stated or the matrix elements
               are not of the same size
    ZeroDivisionError: if div is zero

    Returns: a new matrix holding the results

    """
    workmat = []
    WrongType = False
    TooLong = False
    i = 0
    if isinstance(matrix, list):
        if matrix == []:
            WrongType = True
        for x in range(len(matrix)):
            if isinstance(matrix[x], list):
                workmat.append([])
                for y in range(len(matrix[x])):
                    if matrix[x] == []:
                        WrongType = True
                    if (
                            isinstance(matrix[x][y], int) or
                            isinstance(matrix[x][y], int)
                    ):
                        workmat[x].append(matrix[x][y])
                    else:
                        WrongType = True
                    if x == 0 and y == 0:
                        i = len(matrix[x])
                    else:
                        if not i == len(matrix[x]):
                            TooLong = True
            else:
                WrongType = True
    else:
        WrongType = True
    if WrongType:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if TooLong:
        raise TypeError(
            "Each row of the matrix must have the same size")
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError(
            "div must be a number")
    if div == 0:
        raise ZeroDivisionError(
            "division by zero")

    for x in range(len(workmat)):
        for y in range(len(workmat[x])):
            workmat[x][y] = round((workmat[x][y] / div), 2)
    return workmat
