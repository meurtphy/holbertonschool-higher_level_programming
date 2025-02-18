Rapport sur HTTP, HTTPS et les Requêtes HTTP

1. Introduction

HTTP (HyperText Transfer Protocol) et HTTPS (HTTP Secure) sont des protocoles essentiels pour la communication sur le web. Cet exercice permet de comprendre leurs différences, la structure des requêtes/réponses HTTP et les méthodes/codes de statut courants.

2. Différences entre HTTP et HTTPS

HTTP : Transfère les données en clair, sans chiffrement.

HTTPS : Version sécurisée avec chiffrement SSL/TLS, protégeant la confidentialité des données.

Différences principales :

Chiffrement des données (HTTPS uniquement)

Utilisation d'un certificat SSL/TLS (HTTPS)

Présence d'un cadenas dans la barre d'adresse pour HTTPS

3. Structure des Requêtes et Réponses HTTP

Requête HTTP :

Méthode : Action demandée (GET, POST, etc.)

URL/Path : Adresse de la ressource

En-têtes (Headers) : Informations supplémentaires (type de contenu, autorisation, etc.)

Corps (Body) : Données envoyées (surtout en POST, PUT)

Réponse HTTP :

Code de statut : Indique le résultat de la requête (200, 404, etc.)

En-têtes (Headers) : Métadonnées sur la réponse

Corps (Body) : Contenu renvoyé (comme une page HTML ou des données JSON)

4. Méthodes et Codes de Statut HTTP Courants

Méthodes HTTP :

GET : Récupérer des données (ex : afficher une page)

POST : Envoyer des données au serveur (ex : soumettre un formulaire)

PUT : Mettre à jour une ressource existante

DELETE : Supprimer une ressource

Codes de Statut HTTP :

200 OK : Requête réussie (ex : page chargée avec succès)

301 Moved Permanently : Redirection permanente (ex : changement d’URL)

404 Not Found : Ressource introuvable (ex : page inexistante)

500 Internal Server Error : Erreur serveur (ex : problème interne)

5. Outils Recommandés

Wireshark : Pour observer le trafic réseau HTTP/HTTPS (avec autorisation)

Inspecteur Réseau du Navigateur : Pour visualiser les requêtes et réponses (Onglet "Network")

6. Conclusion

Cet exercice a permis de différencier HTTP et HTTPS, de comprendre la structure des échanges HTTP et de reconnaître les méthodes et codes de statut principaux. Cette maîtrise est fondamentale pour tout travail sur les services web et les APIs.