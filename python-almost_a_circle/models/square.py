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
