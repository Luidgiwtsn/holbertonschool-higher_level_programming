#!/usr/bin/env python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Lit et retourne la liste des produits depuis products.json"""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Lit et retourne la liste des produits depuis products.csv"""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id":       int(row["id"]),
                "name":     row["name"],
                "category": row["category"],
                "price":    float(row["price"])
            })
    return products


def read_sql():
    """Lit et retourne la liste des produits depuis products.db"""
    conn = sqlite3.connect('products.db')

    # row_factory permet d'accéder aux colonnes par leur nom (comme un dict)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()

    # Conversion en liste de dictionnaires
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    # Récupération des paramètres dans l'URL
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Choix de la source de données
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        try:
            data = read_sql()
        except Exception as e:
            return render_template('product_display.html',
                                   error=f"Database error: {str(e)}")
    else:
        return render_template('product_display.html',
                               error="Wrong source. Use 'json', 'csv' or 'sql'.")

    # Filtrage par id si fourni
    if product_id:
        data = [p for p in data if p["id"] == int(product_id)]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found.")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
