#!/usr/bin/python3
""" DOCUMENTATION """

class BaseGeometry:
    """ DOCUMENTATION """

    def __init__(self, width, height):
            self.integer_validator("width", width)
            self.__width = width
            self.integer_validator("height", height)
            self.__height = height
    
    def area(self):
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        elif (value < 1):
            raise ValueError(f"{name} must be greater than 0")
    
    def getwidth(self):
        return (self.__width)
   
    def getheight(self):
        return (self.__height)


class Rectangle(BaseGeometry):
    """ DOCUMENTATION """

    def __init__(self, width, height):
         super().__init__(width, height)
         
    def __str__(self):
        return(f"[Rectangle] {self.getwidth()}/{self.getheight()}")
    
    def area(self):
        return (self.getwidth() * self.getheight())

class Square(Rectangle):
    """ DOCUMENTATION """

    def __init__(self, size):
         super().__init__(size, size)
    
    def __str__(self):
        return(f"[Square] {self.getwidth()}/{self.getheight()}")
    
    def area(self):
        return (self.getwidth() * self.getheight())

s = Square(13)

print(s)
print(s.area())