#!/usr/bin/python3
""" Script that lists all cities of a state using MySQLdb """
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

    # Requête SQL sécurisée pour éviter les injections
    query = "SELECT cities.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s ORDER BY cities.id ASC"

    cur.execute(query, (sys.argv[4],))

    # Récupérer les résultats et les afficher
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))

    # Fermer les connexions
    cur.close()
    db.close()
