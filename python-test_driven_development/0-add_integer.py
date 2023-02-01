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

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
