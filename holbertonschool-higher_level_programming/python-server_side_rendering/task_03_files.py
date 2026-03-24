#!/usr/bin/env python3
import json
import csv
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
            # CSV lit tout en string → on convertit id et price
            products.append({
                "id":       int(row["id"]),
                "name":     row["name"],
                "category": row["category"],
                "price":    float(row["price"])
            })
    return products


@app.route('/products')
def products():
    # Récupération des paramètres dans l'URL
    source = request.args.get('source')   # ?source=json ou ?source=csv
    product_id = request.args.get('id')   # ?id=1 (optionnel)

    # Vérification de la source
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        # Source invalide → message d'erreur
        return render_template('product_display.html',
                               error="Wrong source. Use 'json' or 'csv'.")

    # Filtrage par id si fourni
    if product_id:
        data = [p for p in data if p["id"] == int(product_id)]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found.")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
