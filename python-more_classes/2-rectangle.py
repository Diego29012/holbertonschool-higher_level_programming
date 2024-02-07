#!/usr/bin/python3
"""this module defines a rectangle class"""


class Rectangle:
    """this defines the class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
        def area(self):
        return self._height * self._width

    def perimeter(self):
        if self._height == 0 or self._width == 0:
            perimeter = 0
            return perimeter
        else:
            return 2 *(self.__height + self.__width)
