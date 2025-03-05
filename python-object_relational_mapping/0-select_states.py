#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)


    # Création d'un curseur pour exécuter la requête
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération et affichage des résultats
    for row in cursor.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
