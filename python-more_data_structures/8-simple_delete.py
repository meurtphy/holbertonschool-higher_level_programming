#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.
    - If the key exists, it is removed.
    - If the key does not exist, the dictionary remains unchanged.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
