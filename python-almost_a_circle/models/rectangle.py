class Rectangle(Base):
    """comments"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """comments"""
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """comments"""
        return self._width

    @width.setter
    def width(self, value):
        """comments""" 
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self._width = value

    @property
    def height(self):
        """comments"""
        return self._height

    @height.setter
    def height(self, value):
        """comments"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self._height = value

    @property
    def x(self):
        """comments"""
        return self._x

    @x.setter
    def x(self, value):
        """comments"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self._x = value

    @property
    def y(self):
        """comments"""
        return self._y

    @y.setter
    def y(self, value):
        """comments"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self._y = value

    def area(self):
        """Return the area of rectangle, how? width mult height"""
        return self.width * self.height

