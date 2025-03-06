#!/usr/bin/python3
""" Script that lists all cities of a given state from the database hbtn_0e_4_usa """
import MySQLdb
import sys

if __name__ == "__main__":
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

    # Requête SQL sécurisée avec un paramètre
    cur.execute("SELECT cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))

    # Récupération des résultats
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))

    # Fermeture de la connexion
    cur.close()
    db.close()
