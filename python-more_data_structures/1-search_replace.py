#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Returns a new list where all occurrences of 'search' in 'my_list'
    are replaced with 'replace'. The original list is not modified.
    """
    # Create a new list using a list comprehension:
    return [replace if item == search else item for item in my_list]
