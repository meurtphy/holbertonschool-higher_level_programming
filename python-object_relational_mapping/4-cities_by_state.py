#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def list_cities():
    """Function that lists all cities with their state names"""
    if len(sys.argv) != 4:
        return

    # Connexion à la base de données
    db = MySQLdb.connect(
    host="172.18.0.2",  # Mets l'IP récupérée ici
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    port=3306
 )


    # Création du curseur
    cur = db.cursor()

    # Requête SQL pour lister toutes les villes avec leur état
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    cur.execute(query)

    # Afficher les résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities()
