#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("$")
        return

    for arr in matrix:
        for arr2 in arr:
            if (arr2 == arr[-1]):
                print("{:d}".format(arr2), end="$\n")
            else:
                print("{:d}".format(arr2), end=" ")
