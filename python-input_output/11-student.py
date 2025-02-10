#!/usr/bin/python3
"""Student class with JSON conversion and reload functionality."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes whose names are in
        this list must be retrieved. Otherwise, all attributes must be
        retrieved.
        """
        if (isinstance(attrs, list)
                and all(isinstance(attr, str) for attr in attrs)):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary with key/value pairs to update the
                Student.
        """
        for key, value in json.items():
            setattr(self, key, value)
