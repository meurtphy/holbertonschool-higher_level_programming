#!/usr/bin/python3
"""
Module qui divise tous les éléments d'une matrice.
"""


def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur donné.

    Args:
        matrix (list of lists): Une liste de listes contenant des entiers ou des flottants.
        div (int or float): Le diviseur.

    Returns:
        list of lists: Une nouvelle matrice où chaque élément est divisé par `div`,
        arrondi à 2 décimales.

    Raises:
        TypeError: Si la matrice n'est pas une liste de listes d'entiers ou de flottants,
                   si les lignes de la matrice n'ont pas la même taille,
                   ou si `div` n'est pas un entier ou un flottant.
        ZeroDivisionError: Si `div` est égal à 0.
    """
    error_message = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(item, (int, float)) for row in matrix for item in row)):
        raise TypeError(error_message)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
