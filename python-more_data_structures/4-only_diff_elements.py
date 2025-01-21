#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.
    """
    # Use the symmetric difference operator to find elements in either set but not both
    return set_1 ^ set_2