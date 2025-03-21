#!/usr/bin/env python3
"""
task_04_db.py
Flask app pour afficher des produits depuis JSON, CSV ou SQLite.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    """Lit et retourne la liste de produits depuis 'products.json'."""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    """Lit et retourne la liste de produits depuis 'products.csv'."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convertir id en int si présent
                if 'id' in row:
                    row['id'] = int(row['id'])
                # Convertir price en float
                if 'price' in row:
                    row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        pass
    return products

def read_sql():
    """Lit et retourne la liste de produits depuis la base SQLite 'products.db'."""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        # Transformer chaque ligne en dict
        products = []
        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })
        return products
    except Exception:
        # Si souci d'accès à la DB, on renvoie une liste vide
        return []

@app.route('/products')
def products():
    """Route principale pour afficher les produits depuis la source choisie."""
    source = request.args.get('source')   # ?source=json ou csv ou sql
    product_id = request.args.get('id')   # ?id=XXX (optionnel)

    # Sélection de la source
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        # Source invalide -> message d'erreur explicite
        return render_template('product_display.html', error="Wrong source")

    # data doit être une liste de dict. On vérifie si c'est vide => possible
    if not isinstance(data, list):
        # Au cas où read_sql() ou autre renvoie pas une liste
        return render_template('product_display.html', error="Wrong source")

    # Filtrage par ID si paramètre 'id' est présent
    if product_id:
        try:
            pid = int(product_id)
            data = [p for p in data if p.get("id") == pid]
            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            # ID n'est pas un nombre
            return render_template('product_display.html', error="Product not found")

    # On renvoie la page avec la liste (ou vide si pas d'erreur)
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
