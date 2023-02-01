#!/usr/bin/python3
"""A Python Script"""


class Square:
    """
    Make a Square
    Args:
        __size (int): size.
    """

    def __init__(self, size=0, position=(0, 0)):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (position[1] * position[0] < 0):
            raise ValueError("size must be an integer")
        else:
            self.__position = position

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

    def getposition(self):
        return (self)

    def setposition(self, value):
        if (value[1] * value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    position = property(getposition, setposition)

    def my_print(self):
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for space in range(self.__position[0]):
                print("", end=" ")
            for i2 in range(self.__size):
                print("#", end="")
            print()
