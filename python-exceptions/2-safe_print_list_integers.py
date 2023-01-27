#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        if len(my_list) == 0:
            return (0)

        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        print()
        return (my_list[x])
    except:
        return (my_list[-1])
