#!/usr/bin/python3
"""A Python Script"""


class Rectangle:
    """Make a Rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = None
        self.__height = None
        self.setwidth(width)
        self.setheight(height)
        Rectangle.number_of_instances += 1

    def getwidth(self):
        return (self.__width)

    def setwidth(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    width = property(getwidth, setwidth)

    def getheight(self):
        return (self.__height)

    def setheight(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    height = property(getheight, setheight)
