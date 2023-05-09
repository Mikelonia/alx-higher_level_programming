#!/usr/bin/python3
"""Rectangle module by Okpako Michael"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class by Okpako"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize rectangle class by Okpako Michael"""

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter function by Okpako Michael"""

        return self.width

    @size.setter
    def size(self, size):
        """Setter function by Okpako Michael"""

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute by Okpako Michael"""

        args_list = ["id", "size", "x", "y"]

        if args and len(args) != 0:
            for a_el in range(len(args)):
                setattr(self, args_list[a_el], args[a_el])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation by Okpako Michael"""

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Str representation of square by Okpako Michael"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
