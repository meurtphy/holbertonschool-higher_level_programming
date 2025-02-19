from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire vide pour stocker les utilisateurs
users = {}

### ✅ Route principale "/"
@app.route("/")
def home():
    return "Welcome to the Flask API!"

### ✅ Endpoint "/status" qui retourne "OK"
@app.route("/status")
def status():
    return "OK"

### ✅ Endpoint "/data" qui retourne la liste des usernames
@app.route("/data")
def get_users():
    return jsonify(list(users.keys()))  # Ex: ["alice", "bob"]

### ✅ Endpoint "/users/<username>" pour récupérer un utilisateur spécifique
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404  # Code 404 si l'utilisateur n'existe pas

### ✅ Endpoint "/add_user" pour ajouter un utilisateur via une requête POST
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()  # Récupérer les données JSON envoyées

    # Vérifier si l'username est fourni
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400  # Code 400 si l'username est absent

    username = data["username"]

    # 🚨 **Correction : Vérifier si l'utilisateur existe déjà**
    if username in users:
        return jsonify({"error": "User already exists"}), 400  # Code 400 pour doublon

    # Ajouter l'utilisateur dans le dictionnaire
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201  # Code 201 pour création réussie


    # Ajouter l'utilisateur dans le dictionnaire
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201  # Code 201 pour création réussie

# Lancer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)  # `debug=True` permet le rechargement automatique du serveur
