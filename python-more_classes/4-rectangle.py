#!/usr/bin/python3
"""Module that defines a Rectangle class with area, perimeter,
and string representation methods"""


class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle instance.

        Args:
            width (int): The width of the rectangle sides.
            height (int): The height of the rectangle sides.
        """
        self.width = width
        self.height = height

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
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either
                 width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle using the `#` character.

        Returns:
            str: The rectangle represented by `#` characters, or an empty
                 string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_rows = []
        for _ in range(self.__height):
            rectangle_rows.append('#' * self.__width)
        return "\n".join(rectangle_rows)

    def __repr__(self):
        """
        Return the official string representation of the Rectangle.

        This representation can be used with eval() to recreate the object.

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
