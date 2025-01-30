#!/usr/bin/python3
"""Module that defines a Rectangle class with area, perimeter,
string representation methods, instance tracking, and customizable print symbols."""


class Rectangle:
    """Represents a rectangle with width and height."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle instance.

        Args:
            width (int): The width of the rectangle sides. Defaults to 0.
            height (int): The height of the rectangle sides. Defaults to 0.
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
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        fusion
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle

        Returns:
            str: The rectangle represented by `print_symbol`
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)

        rectangle_rows = []
        for _ in range(self.__height):
            rectangle_rows.append(symbol * self.__width)
        return "\n".join(rectangle_rows)

    def __repr__(self):
        """
        Return the official string representation
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Destructor for the Rectangle instance.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
