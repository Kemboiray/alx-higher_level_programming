#!/usr/bin/python3
"""Defines ``Square``, a direct subclass of ``Rectangle``"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Models a square object"""
    def __init__(self, size: int, x: int = 0, y: int = 0, id: int = None):
        """Class constructor
        Args:
            size: side length of square
            x, y: positional coordinates
            id: onject counter
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for ``size`` """
        return self.width

    @size.setter
    def size(self, value):
        """setter method for ``size`` """
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y}\
 - {self.width}"
