#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("$")
        return

    for arr in matrix:
        for arr2 in arr:
            if (arr2 == arr[-1]):
                print("{:}".format(arr2), end="$\n")
            else:
                print("{:}".format(arr2), end=" ")


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()