#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name_searched>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statenamesearch = sys.argv[4]

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
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}%'".format(statenamesearch))

    # Récupération de tous les résultats
    rows = cursor.fetchall()

    # Affichage de chaque ligne (tuple)
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
