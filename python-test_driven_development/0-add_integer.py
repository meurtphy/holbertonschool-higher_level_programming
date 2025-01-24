#!/usr/bin/python3
"""
Module qui contient la fonction add_integer.
"""

def add_integer(a, b=98):
    """
    Ajoute deux entiers.

    Args:
        a (int or float): Le premier nombre à ajouter.
        b (int or float, optional): Le deuxième nombre à ajouter. Par défaut, 98.

    Returns:
        int: La somme de a et b.

    Raises:
        TypeError: Si a ou b ne sont pas des entiers ou des flottants.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
