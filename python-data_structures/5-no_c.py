#!/usr/bin/python3
def no_c(my_string):
    finder = my_string.lower().find('c')
    while finder != -1:
        my_string = my_string[:finder] + my_string[finder + 1:]
        finder = my_string.lower().find('c')
    return (my_string)
