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
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): Size of the square.
        """
        self.__size = size
