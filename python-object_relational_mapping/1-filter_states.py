#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="127.0.0.1",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Création du curseur pour exécuter des requêtes
    cur = db.cursor()

    # Requête SQL pour récupérer les états commençant par 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Récupérer et afficher les résultats
    for row in cur.fetchall():
        print(row)

    # Fermer le curseur et la connexion
    cur.close()
    db.close()
