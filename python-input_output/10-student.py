#!/usr/bin/python3
"""Student class with JSON conversion."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of student.
        If attrs is a list of strings, only retrieve matching attributes.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key)
                    for key in attrs
                    if hasattr(self, key)}
        return self.__dict__
