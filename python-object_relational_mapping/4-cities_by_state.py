#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création du curseur
    cur = db.cursor()

    # Exécution de la requête SQL
    query = """SELECT cities.id, cities.name, states.name
               FROM cities JOIN states
               ON cities.state_id = states.id
               ORDER BY cities.id ASC"""
    cur.execute(query)

    # Affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
