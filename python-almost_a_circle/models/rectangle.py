#!/usr/bin/python3
"""_summary_"""


from base import Base

class Rectangle(Base):
    """_summary_"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_"""
        Base.__init__(self, id)
        self.setheight(height)
        self.setwidth(width)
        self.setx(x)
        self.sety(y)

    def __str__(self):
       return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")

    def getwidth(self):
        return (self.__width)

    def setwidth(self, value):
        """_summary_"""
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
        """_summary_"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    height = property(getheight, setheight)

    def getx(self):
        return (self.__x)

    def setx(self, value):
        """_summary_"""
        if (not isinstance(value, int)):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value
    x = property(getx, setx)

    def gety(self):
        return (self.__y)

    def sety(self, value):
        """_summary_"""
        if (not isinstance(value, int)):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    y = property(gety, sety)

    def area(self):
        return self.x * self.y

    def getdisplay (self):
        """doc"""

        rec = ""
        #for space in range(self.y):
        #    rec += "\n"
        for i in range(self.height):
            #for space in range(self.x):
            #    rec += " "
            for i2 in range(self.width):
                rec += "#"
            rec += "\n" if i < self.height - 1 else ""
        return (rec)

    def display(self):
        print(self.getdisplay())
