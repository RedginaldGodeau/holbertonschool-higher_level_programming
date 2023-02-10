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


class Rectangle(BaseGeometry):
    """ DOCUMENTATION """

    def __init__(self, width, height):
         super().__init__(width, height)