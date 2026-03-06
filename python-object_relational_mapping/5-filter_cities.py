#!/usr/bin/env python3
"""
script that  lists all cities from the database hbtn_0e_4_usa
Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> 
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]

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
    cursor.execute("SELECT c.name FROM cities c JOIN states s ON c.state_id = s.id WHERE s.name = %s ORDER BY c.id ASC",(statename,))

    # Récupération de tous les résultats
    rows = cursor.fetchall()

    # Affichage de chaque ligne (tuple)
    
    print(", ".join(row[0] for row in rows))

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
