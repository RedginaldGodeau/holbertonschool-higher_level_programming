#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if x == 0 or not my_list:
        print("0")
        return (0)

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except:
            print("", end="")
    print()

    try:
        return (my_list[x])
    except:
        return (my_list[-1])
