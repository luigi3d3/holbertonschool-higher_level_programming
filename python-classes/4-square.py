#!/usr/bin/python3

"""Square class"""


class Square:
    """
    Class Square that defines a square.

    Attributes:
        __size (int): Private instance attribute for the size of the square.

    Methods:
        __init__(self, size): Initializes a new instance of the Square class.
        area(self): Computes the area of the square.
        size(self, value): Getter and setter for the size attribute.
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
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Parameters:
            value (int): Size to set for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
