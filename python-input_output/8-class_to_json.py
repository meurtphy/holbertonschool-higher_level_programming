#!/usr/bin/python3
"""
Module that returns the dictionary description
"""


def class_to_json(obj):
    """
    Returns the dictionary description
    """
    return obj.__dict__
