#!/usr/bin/python3
"""
Module qui contient la fonction add_integer.
"""


def add_integer(a, b=98):
    """
    Ajoute deux nombres après les avoir convertis en entiers.

    Args:
        a (int or float): Le premier nombre.
        b (int or float, optional): Le deuxième nombre, par défaut 98.

    Returns:
        int: La somme des deux nombres convertis en entiers.

    Raises:
        TypeError: Si a ou b ne sont ni des entiers
        ni des flottants.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return a + b
