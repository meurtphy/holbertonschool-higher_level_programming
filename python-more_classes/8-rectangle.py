#!/usr/bin/python3
"""Module that defines a Rectangle class with area, perimeter,
string representation methods, instance tracking, customizable print symbols, and comparison."""


class Rectangle:
    """Represents a rectangle with width and height."""

    number_of_instances = 0  # Public class attribute to track instances
    print_symbol = '#'       # Public class attribute for string representation

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle instance.

        Args:
            width (int): The width of the rectangle sides. Defaults to 0.
            height (int): The height of the rectangle sides. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment on new instance

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
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # Convert print_symbol to string in case it's not
        symbol = str(self.print_symbol)

        rectangle_rows = []
        for _ in range(self.__height):
            rectangle_rows.append(symbol * self.__width)
        return "\n".join(rectangle_rows)

    def __repr__(self):
        """
        Return the official string representation of the Rectangle.

        This representation can be used with eval() to recreate the object.

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Destructor for the Rectangle instance.

        Prints a message when an instance is about to be destroyed and
        decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement on instance deletion

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle.
            TypeError: If rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
