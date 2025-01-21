#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.
    Keys are sorted alphabetically, and values are printed in the format key: value.
    """
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
