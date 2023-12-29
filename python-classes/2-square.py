#!/usr/bin/python3

"""Square class"""


class Square:
    """
    Class Square that defines a square.

    Attributes:
        __size (int): Private instance attribute for the size of the square.

    Methods:
        __init__(self, size): Initializes a new instance of the Square class.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): Size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
