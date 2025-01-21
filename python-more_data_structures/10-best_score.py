#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in the dictionary.
    If no scores are found or the dictionary is None, returns None.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
