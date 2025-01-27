#!/usr/bin/python3
"""2-square.py"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Initialize the square with a private size attribute.
        Validate that size is an integer and >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
