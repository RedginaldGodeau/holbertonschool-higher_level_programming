#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_table = []
    
    for item in matrix:
        new_table.append(item.copy());
    
    for item in new_table:
        for i in range(len(item)):
            item[i] **=2;

    return (new_table);
