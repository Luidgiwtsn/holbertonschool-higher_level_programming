#!/usr/bin/env python3
"""Module pour récupérer et manipuler des données depuis JSONPlaceholder."""

import csv
import requests


def fetch_and_print_posts():
    """Récupère tous les posts de JSONPlaceholder et affiche leurs titres.

    Envoie une requête GET à l'API JSONPlaceholder pour obtenir la liste
    complète des posts. Affiche le code de statut de la réponse, puis,
    si la requête est réussie, affiche le titre de chaque post.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Récupère tous les posts de JSONPlaceholder et les sauvegarde en CSV.

    Envoie une requête GET à l'API JSONPlaceholder pour obtenir la liste
    complète des posts. Si la requête est réussie, structure les données
    dans une liste de dictionnaires contenant les clés 'id', 'title' et
    'body', puis écrit ces données dans un fichier CSV nommé 'posts.csv'.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
