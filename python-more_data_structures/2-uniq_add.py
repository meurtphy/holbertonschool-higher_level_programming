#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.
    Each integer is only considered once, even if it appears multiple times.
    """
    return sum(set(my_list))
