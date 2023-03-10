#!/usr/bin/python3
"""A Python Script"""


class Square:
    """
    Make a Square
    Args:
        __size (int): size.
    """

    def __init__(self, size=0):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def getsize(self):
        return (self.__size)

    def setsize(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        return (self.__size)

    size = property(getsize, setsize)

    def my_print(self):
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for i2 in range(self.__size):
                print("#", end="")
            print()
