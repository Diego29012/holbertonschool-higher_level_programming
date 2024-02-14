#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The square of Rectangule """
    def __init__(self, size, x=0, y=0, id=None):
        """ the rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Print [Square] (<id>) <x>/<y> - <size> """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """square size."""
        return self.width

    @size.setter
    def size(self, value):
        """square size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns an argument to the all attribute"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        for d, k in kwargs.items():
            setattr(self, d, k)

    def to_dictionary(self):
        """Return dictionary representation"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
