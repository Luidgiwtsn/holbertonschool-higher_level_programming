#!/usr/bin/env python3
"""
Module implémentant une API REST simple avec Flask.

Ce module définit plusieurs routes pour gérer des utilisateurs
stockés en mémoire sous forme de dictionnaire Python.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire de stockage des utilisateurs en mémoire
# Clé : username (str), Valeur : dictionnaire contenant les infos
users = {}


@app.route("/")
def home():
    """
    Route racine de l'API.

    Returns:
        str: Message de bienvenue.
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Route de vérification de l'état de l'API.

    Returns:
        str: La chaîne "OK".
    """
    return "OK"


@app.route("/data")
def data():
    """
    Route retournant la liste de tous les usernames enregistrés.

    Returns:
        Response: Réponse JSON contenant une liste de usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Route retournant les informations d'un utilisateur spécifique.

    Args:
        username (str): Le nom d'utilisateur à rechercher.

    Returns:
        Response: Réponse JSON avec les données de l'utilisateur,
                  ou une erreur 404 si l'utilisateur n'existe pas.
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Route permettant d'ajouter un nouvel utilisateur via une requête POST.

    Le corps de la requête doit être un JSON valide contenant au minimum
    le champ "username".

    Exemple de corps attendu::

        {
            "username": "alice",
            "name": "Alice",
            "age": 25,
            "city": "San Francisco"
        }

    Returns:
        Response: Réponse JSON avec un message de confirmation et les données
                  de l'utilisateur ajouté (code 201), ou une erreur adaptée :
                  - 400 si le JSON est invalide ou si le username est absent.
                  - 409 si le username existe déjà.
    """
    # Vérification que le corps de la requête est un JSON valide
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Vérification de la présence du champ username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Vérification que le username n'existe pas déjà
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Ajout de l'utilisateur dans le dictionnaire
    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
