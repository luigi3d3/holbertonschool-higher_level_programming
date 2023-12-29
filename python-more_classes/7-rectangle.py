#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """Rectangle class with width, height, area, and perimeter attributes."""

    number_of_instances = 0
    print_symbol = "#"

    def _init_(self, width=0, height=0):
        """
        Initialize a Rectangle instance with optional width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with type and value validation.

        Args:
            value (int): The width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with type and value validation.

        Args:
            value (int): The height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self._width + self._height)

    def _str_(self):
        """
        Return a string representation of the rectangle using print_symbol.

        Returns:
            str: A string representation of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return ("\n".join([str(self.print_symbol) * self._width] * self._height))

    def _repr_(self):
        """
        Return a string representation of the rectangle for eval().

        Returns:
            str: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self._width, self._height)

    def _del_(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
