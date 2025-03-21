from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Flask App! Visit /items to see the items list."

@app.route('/items')
def items():
    try:
        # Lire les données depuis le fichier JSON
        with open("items.json", "r") as f:
            data = json.load(f)
            items_list = data.get("items", [])  # Récupérer la liste, ou une liste vide si elle est absente
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []  # En cas d'erreur, utiliser une liste vide

    return render_template("items.html", items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
