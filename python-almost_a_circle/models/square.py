#!/usr/bin/python3
""" docs """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle

    Args:
        Base (self): Parent class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """__init__

        Args:
            size (int / float)
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (int, optional): Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__

        Returns:
            string: Info of class
        """
        return f"[Square] ({self.id})\
 {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """update

        Desc:
            Update value of class
        """
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)
    
    def to_dictionary(self):
        """to_dictionary

        Returns:
            dictionnary: get info for class
        """
        return {
            "id": self.id, 
            "size": self.size, 
            "x": self.x, 
            "y": self.y
        }

    def getsize(self):
        """getsize

        Returns:
            int: get size
        """
        return self.__height

    def setsize(self, value):
        """setsize

        Args:
            value (int): value size

        Raises:
            TypeError: size must be an integer
            ValueError: size must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        self.height = value
        self.width = value

    size = property(getsize, setsize)
