#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        if not my_list:
            return (0)

        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        print()
        return (my_list[x])
    except:
        return (my_list[-1])

my_list = []

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))