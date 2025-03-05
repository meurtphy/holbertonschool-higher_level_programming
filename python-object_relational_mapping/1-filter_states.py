#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states():
    """Function that lists states starting with 'N'"""
    if len(sys.argv) != 4:
        return

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Création du curseur
    cur = db.cursor()

    # Exécuter la requête SQL avec LIKE BINARY pour la casse
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    # Afficher les résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
