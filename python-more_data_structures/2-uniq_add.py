#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.
    Each integer is only considered once, even if it appears multiple times.
    """
    # Use a set to eliminate duplicates and sum the unique values
    return sum(set(my_list))
