Rapport sur l'Utilisation de curl pour Interagir avec des APIs

1. Introduction

curl (Client URL) est un outil en ligne de commande permettant de transférer des données à l'aide de divers protocoles (HTTP, HTTPS, FTP, etc.). Cet outil est essentiel pour tester des APIs et diagnostiquer les problèmes de serveur.

2. Installation et Vérification

Installation de curl

Linux/Mac : curl est souvent préinstallé. Sinon :

sudo apt update && sudo apt install curl  # Ubuntu/Debian
brew install curl  # Mac avec Homebrew

Windows : Installer via WSL ou curl.se.

Vérification de l'Installation

Commande :

curl --version

Résultat attendu : Affichage de la version de curl et des protocoles pris en charge.

3. Requêtes API avec curl

3.1. Récupérer une Page Web

Commande :

curl http://example.com

Résultat : Contenu HTML brut de la page.

3.2. Effectuer une Requête GET sur une API

API de test : JSONPlaceholder
Commande :

curl https://jsonplaceholder.typicode.com/posts

Résultat : JSON contenant une liste de publications :

[
  {"userId": 1, "id": 1, "title": "Titre", "body": "Contenu..."},
  {"userId": 1, "id": 2, "title": "Un autre titre", "body": "Autre contenu..."}
]

3.3. Afficher Uniquement les En-têtes (Headers)

Commande :

curl -I https://jsonplaceholder.typicode.com/posts

Résultat attendu : En-têtes de la réponse HTTP :

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 6553

3.4. Effectuer une Requête POST (Envoyer des Données)

Commande :

curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

Résultat attendu (simulation) :

{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}

4. Conseils Supplémentaires

Formater les Résultats JSON avec jq :

sudo apt install jq  # Linux
brew install jq      # Mac
curl https://jsonplaceholder.typicode.com/posts | jq

Documentation : Voir Everything curl et JSONPlaceholder.

5. Conclusion

Cet exercice a permis de maîtriser les bases de curl pour interagir avec des APIs : récupération de données, affichage des en-têtes et envoi de données. Ces compétences sont essentielles pour tester et déboguer des services web de manière efficace.