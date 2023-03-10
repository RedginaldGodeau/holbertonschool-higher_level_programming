#!/usr/bin/python3
""" DOCUMENTATION """

class BaseGeometry:
    """ DOCUMENTATION """
    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if (not isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
        elif (value < 1):
            raise ValueError(f"{name} must be greater than 0")
