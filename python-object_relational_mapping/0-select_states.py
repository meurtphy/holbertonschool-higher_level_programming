#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # 1. Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 2. Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # 3. Création d’un curseur pour exécuter les requêtes
    cur = db.cursor()

    # 4. Exécution de la requête
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    # 5. Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # 6. Fermeture du curseur et de la connexion
    cur.close()
    db.close()
