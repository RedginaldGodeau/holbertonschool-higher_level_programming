#!/usr/bin/python3
""" Doc """

def matrix_divided(matrix, div):
    """ Doc """

    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    for t in matrix:
        if len(t) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    cpy = []
    for itm in matrix:
        cpy.append(itm.copy())

    for t in cpy:
        for i in range(len(t)):
            if not isinstance(t[i], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            try:
                t[i] = round(t[i] / div, 2)
            except ZeroDivisionError:
                print("division by zero")

    return (cpy)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

