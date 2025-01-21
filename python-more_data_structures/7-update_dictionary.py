#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value pair in a dictionary.
    - If the key exists, its value is updated.
    - If the key does not exist, it is added.
    """
    a_dictionary[key] = value
    return a_dictionary