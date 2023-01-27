#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    size = len(matrix) * len(matrix[0])
    for item in matrix:
        new.append(item.copy())

    for i in range(size):
        col = int(i / 3)
        row = i % 3
        new[col][row] **= 2
    return (new)
