#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à MySQL
    db = MySQLdb.connect(
        host="localhost",  # Laisse "localhost" pour les tests de Holberton
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Création du curseur
    cur = db.cursor()

    # Requête SQL
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture
    cur.close()
    db.close()
