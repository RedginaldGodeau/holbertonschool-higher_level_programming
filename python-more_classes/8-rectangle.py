#!/usr/bin/python3
"""A Python Script"""


class Rectangle:
    """Make a Rectangle"""
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        self.__width = None
        self.__height = None
        self.setwidth(width)
        self.setheight(height)
        Rectangle.number_of_instances += 1
    def __del__(self):
             print('Bye rectangle...')
             Rectangle.number_of_instances -= 1
    def __str__ (self):
        rec = ""
        for i in range(self.getheight()):
            for i2 in range(self.getwidth()):
                rec += str(self.print_symbol)
            rec += "\n" if i < self.getheight() - 1 else ""
        return (rec)
    def __print__ (self):
        return (str(self))
    def __repr__(self):
        return ("Rectangle({}, {})".format(self.getwidth(), self.getheight()))
    
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

    def area(self):
        return (self.getwidth() * self.getheight())
    def perimeter(self):
        if self.getwidth() * self.getheight() == 0:
            return (0)
        return ((self.getwidth() + self.getheight()) * 2)
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1.area() >= rect_2.area():
            return (True)
        return (False)