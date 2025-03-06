#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument (protected from SQL injections).
"""

import MySQLdb
import sys


def safe_filter_states():
    """Function that filters states safely by user input"""
    if len(sys.argv) != 5:
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

    # Récupérer l'argument de l'utilisateur
    state_name = sys.argv[4]

    # Requête SQL sécurisée avec protection contre l'injection SQL
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Afficher les résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
