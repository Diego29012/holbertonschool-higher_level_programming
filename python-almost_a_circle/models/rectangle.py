#!/usr/bin/python3
"""comments"""


from models.base import Base


class Rectangle(Base):
    """comments"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """comments"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """comments"""
        return self.__width

    @width.setter
    def width(self, value):
        """comments""" 
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
         self.__width = value

    @property
    def height(self):
        """comments"""
        return self.__height

    @height.setter
    def height(self, value):
        """comments"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """comments"""
        return self.__x

    @x.setter
    def x(self, value):
        """comments"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """comments"""
        return self.__y

    @y.setter
    def y(self, value):
        """comments"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return the area of rectangle, how? width mult height"""
        return self.width * self.height

    def display(self):
        """Display the rectangle"""
        for lines in range(self.y):
            print()
        for elements in range(self.height):
            print(' ' * self.x + '#' * self.width)
            
    def __str__(self):
        """Return a formatted string"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
            Assigns an argument to each attribute.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        for d, k in kwargs.items():
            setattr(self, d, k)

