#!/usr/bin/python3
"""Creates a Rectangle class"""

class Rectangle:
    """defines a Rectangle class"""
def __init__(self, width=0, height=0):
      self.__width = width
      self.__height = height

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
        

    @height.setter
    def height(self, value):
        
