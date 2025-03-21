from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# 📌 Fonction pour lire un fichier JSON
def read_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# 📌 Fonction pour lire un fichier CSV
def read_csv(file_path):
    try:
        products = []
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])  # Convertir l'ID en entier
                row["price"] = float(row["price"])  # Convertir le prix en float
                products.append(row)
        return products
    except (FileNotFoundError, csv.Error):
        return []

@app.route('/products')
def display_products():
    source = request.args.get("source")  # Récupérer le paramètre source (json/csv)
    product_id = request.args.get("id")  # Récupérer l'ID optionnel

    if source == "json":
        products = read_json("products.json")
    elif source == "csv":
        products = read_csv("products.csv")
    else:
        return render_template("product_display.html", error="❌ Wrong source. Use ?source=json or ?source=csv")

    # 📌 Filtrage par ID si fourni
    if product_id:
        try:
            product_id = int(product_id)  # Convertir l'ID en entier
            products = [p for p in products if p["id"] == product_id]
            if not products:
                return render_template("product_display.html", error="❌ Product not found.")
        except ValueError:
            return render_template("product_display.html", error="❌ Invalid ID format.")

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
