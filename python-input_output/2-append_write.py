#!/usr/bin/python3
"""
coucou1
"""


def append_write(filename="", text=""):
    """
    Writes a string to a text file (UTF8)

    :param filename: Name of the file.
    :param text: String to write.
    :return: Number of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
