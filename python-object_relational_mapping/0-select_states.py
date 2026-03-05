#!/usr/bin/env python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion au serveur MySQL (localhost, port 3306)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Création du curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Exécution de la requête SQL
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération de tous les résultats
    rows = cursor.fetchall()

    # Affichage de chaque ligne (tuple)
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
