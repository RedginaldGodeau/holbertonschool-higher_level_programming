#!/usr/bin/python3
""" docs """
from models.base import Base


class Rectangle(Base):
    """Rectangle

    Args:
        Base (self): Parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__

        Args:
            width (int / float)
            height (int / float)
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (int, optional): Defaults to None.
        """
        Base.__init__(self, id)
        self.setheight(height)
        self.setwidth(width)
        self.setx(x)
        self.sety(y)

    def __str__(self):
        """__str__

        Returns:
            string: Info of class
        """
        return f"[Rectangle] ({self.id})\
 {self.x}/{self.y} - {self.width}/{self.height}"

    def getwidth(self):
        """getwidth

        Returns:
            int: Width of Class
        """
        return self.__width

    def setwidth(self, value):
        """setwidth

        Args:
            value (int): value width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    width = property(getwidth, setwidth)

    def getheight(self):
        """getheight

        Returns:
            int: get height
        """
        return self.__height

    def setheight(self, value):
        """setheight

        Args:
            value (int): value height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    height = property(getheight, setheight)

    def getx(self):
        """getx

        Returns:
            int: X
        """
        return self.__x

    def setx(self, value):
        """setx

        Args:
            value (int): value x

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    x = property(getx, setx)

    def gety(self):
        """gety

        Returns:
            int: get y
        """
        return self.__y

    def sety(self, value):
        """sety

        Args:
            value (int): value y

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    y = property(gety, sety)

    def area(self):
        """area

        Returns:
            int: get area of class
        """
        return self.x * self.y

    def getdisplay(self):
        """getdisplay

        Returns:
            _type_: Rectangle printed
        """
        rec = ""
        # for space in range(self.y):
        #    rec += "\n"
        for i in range(self.height):
            # for space in range(self.x):
            #    rec += " "
            for i2 in range(self.width):
                rec += "#"
            rec += "\n" if i < self.height - 1 else ""
        return rec

    def display(self):
        """display
            print rectangle
        """
        print(self.getdisplay())
