#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument (safe from SQL injections).
"""

import MySQLdb
import sys


def filter_states_by_user_input():
    """Function that filters states by user input"""
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

    # Requête SQL avec format (ATTENTION : Risque d'injection SQL, on corrigera après)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )

    cur.execute(query)

    # Afficher les résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_user_input()
