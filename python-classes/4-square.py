#!/usr/bin/python3
"""4-square.py"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Initialize the square with a private size attribute.
        Use the property setter to validate and set size.
        """
        self.size = size  # This calls the size setter for validation.

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size.
        Validates that size is an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2
