#!/usr/bin/python3
"""Module containing text_indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ?, and :.

    Args:
        text (str): The input text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
        i += 1
