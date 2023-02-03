#!/usr/bin/python3
"""A Python Script"""


class Rectangle:
    """Make a Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = None
        self.__height = None
        self.setwidth(width)
        self.setheight(height)
    def __del__(self):
             print('Bye rectangle...')
    def __str__ (self):
        rec = ""
        for i in range(self.getheight()):
            for i2 in range(self.getwidth()):
                rec += "#"
            rec += "\n" if i < self.getheight() - 1 else ""
        return (rec)
    def __print__ (self):
        return (str(self))
    def __repr__(self):
        return ("Rectangle({}, {})".format(self.getwidth(), self.getheight()))
    
    def getwidth(self):
        return (self.__width)
    def setwidth(self, value):
        try:
            if (not isinstance(value, int)):
                raise ValueError("width must be an integer")
            elif (value < 0):
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        except Exception as err:
            return (err)
    width = property(getwidth, setwidth)

    def getheight(self):
        return (self.__height)
    def setheight(self, value):
        try:
            if (not isinstance(value, int)):
                raise ValueError("height must be an integer")
            elif (value < 0):
                raise ValueError("height must be >= 0")
            self.__height = value
        except Exception as err:
            return (err)
    height = property(getheight, setheight)

    def area(self):
        return (self.getwidth() * self.getheight())
    def perimeter(self):
        if self.getwidth() * self.getheight() == 0:
            return (0)
        return ((self.getwidth() + self.getheight()) * 2)
