#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        if (not isinstance(a, int)):
            raise TypeError("a must be an integer")
        elif (not isinstance(b, int)):
            raise TypeError("b must be an integer")
        return (a + b)
    except TypeError as err:
        f = open("tests/0-add_integer.txt", "a")
        f.write(str(err))
        f.close()
