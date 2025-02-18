📘 README - Projet d'Apprentissage des Requêtes HTTP avec Python, cURL et Concepts HTTP

📝 Introduction

Ce projet couvre l'apprentissage et la pratique des requêtes HTTP, de l'utilisation de curl et de l'interaction avec des API via Python avec la bibliothèque requests. Il comprend plusieurs étapes allant de la compréhension des concepts de base à la manipulation des réponses API et à l'enregistrement des données dans des fichiers CSV.

📂 Contenu du Projet

1️⃣ - Concepts HTTP et HTTPS

Différences principales entre HTTP et HTTPS :

HTTPS chiffre les données avec SSL/TLS.

HTTP est non sécurisé et transmet les données en clair.

Structure d'une Requête et Réponse HTTP :

Requête : Méthode (GET, POST), URL, En-têtes, Corps.

Réponse : Code de statut (200, 404, 500), En-têtes, Corps.

Méthodes HTTP principales : GET, POST, PUT, DELETE

Codes de statut HTTP courants : 200 (Succès), 301 (Redirection), 404 (Non trouvé), 500 (Erreur serveur)

2️⃣ - Utilisation de curl pour Interagir avec une API

Installation de curl : sudo apt install curl (Linux) ou via curl.se (Windows).

Exemples de commandes curl :

Récupérer une page web : curl http://example.com

Récupérer des posts depuis JSONPlaceholder : curl https://jsonplaceholder.typicode.com/posts

Récupérer uniquement les en-têtes : curl -I https://jsonplaceholder.typicode.com/posts

Envoyer une requête POST avec données :

curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

3️⃣ - Utilisation de Python pour les Requêtes API (requests)

Installation de requests : pip install requests

Création de deux fonctions principales dans task_02_requests.py :

fetch_and_print_posts() : Récupère et affiche les titres des posts.

fetch_and_save_posts() : Récupère les posts et les enregistre dans posts.csv.

📂 Structure du Projet :

restful-api/
   ├── main_02_requests.py
   └── task_02_requests.py

📝 Exécution du script :

python3 main_02_requests.py

✅ Sortie attendue dans le terminal :

Status Code: 200
sunt aut facere repellat provident occaecati...
Les posts ont été sauvegardés dans posts.csv.

📂 Exemple de contenu du fichier CSV (posts.csv) :

id,title,body
1,sunt aut facere...,quia et suscipit...
2,qui est esse,est rerum tempore...

✅ Objectifs Atteints :

Compréhension des requêtes HTTP, des méthodes et des codes de statut.

Utilisation de curl pour interagir avec une API.

Manipulation de données JSON avec Python.

Sauvegarde des données dans un fichier CSV avec Python.

💡 Améliorations Possibles :

Ajouter la gestion des erreurs (try/except) dans les requêtes Python.

Enrichir les commandes curl avec des options avancées.

Formater automatiquement les réponses JSON avec jq.

📚 Ressources Utiles :

MDN Web Docs - HTTP Overview

Everything curl

Python Requests Documentation

JSONPlaceholder - Free Fake API