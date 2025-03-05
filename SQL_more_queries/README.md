SQL More Queries – README
Ce répertoire contient différents scripts SQL permettant de manipuler des bases de données MySQL, illustrant notamment :

La création et la suppression de bases de données.
La création et la gestion de tables, avec différentes contraintes (NOT NULL, UNIQUE, FOREIGN KEY, AUTO_INCREMENT).
Des requêtes avancées sur des bases de données plus complexes (ex. : hbtn_0d_tvshows).
Chaque fichier correspond à un exercice précis, listé ci-dessous.

Table des Matières
Prérequis
Configuration Docker et MySQL
Lancement du conteneur Docker
Vérification du conteneur
Exécution des scripts SQL dans le conteneur
Liste des Exercices (0 à 16)
0. Liste des bases de données (0-list_databases.sql)
1. Création de la base de données (1-create_database_if_missing.sql)
2. Suppression de la base de données (2-remove_database.sql)
3. Liste des tables (3-list_tables.sql)
4. Création de la table first_table (4-first_table.sql)
5. Description complète de first_table (5-full_table.sql)
6. Liste des lignes de first_table (6-list_values.sql)
7. Insertion dans first_table (7-insert_value.sql)
8. Compter les enregistrements (WHERE id = 89) (8-count_89.sql)
9. Création et insertion dans second_table (9-full_creation.sql)
10. Trier par score décroissant (10-top_score.sql)
11. Score >= 10 (11-best_score.sql)
12. Mise à jour du score de "Bob" (12-no_cheating.sql)
13. Suppression (score <= 5) (13-change_class.sql)
14. Moyenne des scores (14-average.sql)
15. Nombre d’enregistrements par score (15-groups.sql)
16. Nom non vide (16-no_link.sql)
Exemples de projets plus avancés (Base hbtn_0d_tvshows)
Commandes Docker utiles
Prérequis
Docker installé et fonctionnel sur votre machine.
MySQL version 8.0 (utilisé dans le conteneur Docker).
Scripts SQL prêts à l’emploi dans ce répertoire.
Configuration Docker et MySQL
Lancement du conteneur Docker
bash
Copier
Modifier
docker run --name mysql_project \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=mydatabase \
    -p 3306:3306 \
    -d mysql:8.0
Ici, on nomme le conteneur mysql_project, on définit le mot de passe root pour MySQL sur root, et on associe le port 3306 de l’hôte à celui du conteneur.

Vérification du conteneur
Pour voir si le conteneur tourne, utilisez :

bash
Copier
Modifier
docker ps
Si vous voyez mysql_project dans la liste, le conteneur est actif. Sinon, démarrez-le :

bash
Copier
Modifier
docker start mysql_project
Exécution des scripts SQL dans le conteneur
Pour exécuter un script SQL dans la base mydatabase (ou autre) du conteneur :

bash
Copier
Modifier
docker exec -i mysql_project \
  mysql -uroot -p'root' [nom_de_la_base] < [script].sql
Pour ouvrir une session interactive MySQL :

bash
Copier
Modifier
docker exec -it mysql_project \
  mysql -uroot -p
Le mot de passe est root (celui défini lors du docker run).

Liste des Exercices (0 à 16)
0. Liste des bases de données (0-list_databases.sql)
But : Afficher toutes les bases de données du serveur MySQL.
Contenu :
sql
Copier
Modifier
SHOW DATABASES;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' < 0-list_databases.sql
1. Création de la base de données (1-create_database_if_missing.sql)
But : Créer la base hbtn_0c_0 si elle n’existe pas déjà.
Contenu :
sql
Copier
Modifier
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' < 1-create_database_if_missing.sql
2. Suppression de la base de données (2-remove_database.sql)
But : Supprimer la base hbtn_0c_0 si elle existe.
Contenu :
sql
Copier
Modifier
DROP DATABASE IF EXISTS hbtn_0c_0;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' < 2-remove_database.sql
3. Liste des tables (3-list_tables.sql)
But : Afficher les tables de la base MySQL (système) ou toute autre base.
Contenu :
sql
Copier
Modifier
SHOW TABLES;
Exécution (ex. sur la base mysql) :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' mysql < 3-list_tables.sql
4. Création de la table first_table (4-first_table.sql)
But : Créer la table first_table dans hbtn_0c_0.
Contenu :
sql
Copier
Modifier
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 4-first_table.sql
5. Description complète de first_table (5-full_table.sql)
But : Afficher la requête de création de first_table.
Contenu :
sql
Copier
Modifier
SHOW CREATE TABLE first_table;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 5-full_table.sql
6. Liste des lignes de first_table (6-list_values.sql)
But : Sélectionner toutes les lignes de first_table.
Contenu :
sql
Copier
Modifier
SELECT * FROM first_table;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 6-list_values.sql
7. Insertion dans first_table (7-insert_value.sql)
But : Insérer une ligne (id=89, name='Best School') dans first_table.
Contenu :
sql
Copier
Modifier
INSERT INTO first_table (id, name)
VALUES (89, 'Best School');
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 7-insert_value.sql
8. Compter les enregistrements (WHERE id = 89) (8-count_89.sql)
But : Compter le nombre d’enregistrements ayant id = 89.
Contenu :
sql
Copier
Modifier
SELECT COUNT(*) FROM first_table WHERE id = 89;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 8-count_89.sql
Pour n’afficher que le chiffre, on peut ajouter :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 8-count_89.sql | tail -1
9. Création et insertion dans second_table (9-full_creation.sql)
But : Créer la table second_table et y insérer plusieurs lignes.
Contenu (extrait) :
sql
Copier
Modifier
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 9-full_creation.sql
10. Trier par score décroissant (10-top_score.sql)
But : Sélectionner score, name de second_table en triant par score DESC.
Contenu :
sql
Copier
Modifier
SELECT score, name FROM second_table ORDER BY score DESC;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 10-top_score.sql
11. Score >= 10 (11-best_score.sql)
But : Afficher les enregistrements dont score >= 10 dans second_table, triés par score DESC.
Contenu :
sql
Copier
Modifier
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 11-best_score.sql
12. Mise à jour du score de "Bob" (12-no_cheating.sql)
But : Mettre le score de “Bob” à 10.
Contenu :
sql
Copier
Modifier
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 12-no_cheating.sql
13. Suppression (score <= 5) (13-change_class.sql)
But : Supprimer les enregistrements dont score <= 5.
Contenu :
sql
Copier
Modifier
DELETE FROM second_table
WHERE score <= 5;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 13-change_class.sql
14. Moyenne des scores (14-average.sql)
But : Calculer la moyenne des scores.
Contenu :
sql
Copier
Modifier
SELECT AVG(score) AS average
FROM second_table;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 14-average.sql
15. Nombre d’enregistrements par score (15-groups.sql)
But : Grouper par score et compter le nombre d’enregistrements.
Contenu :
sql
Copier
Modifier
SELECT score,
       COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 15-groups.sql
16. Nom non vide (16-no_link.sql)
But : Sélectionner les lignes dont name n’est ni NULL ni ''.
Contenu :
sql
Copier
Modifier
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
  AND name != ''
ORDER BY score DESC;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 16-no_link.sql
Exemples de projets plus avancés (Base hbtn_0d_tvshows)
Ensuite, nous avons enchaîné sur des requêtes plus complexes liées à la base hbtn_0d_tvshows :

Import du fichier hbtn_0d_tvshows.sql
Requêtes de jointure (JOIN, LEFT JOIN) pour lister séries et genres, compter, filtrer par condition, etc.
Scripts comme 10-genre_id_by_show.sql, 11-genre_id_all_shows.sql, 12-no_genre.sql, etc.
Pour chacun de ces scripts, la syntaxe d’exécution reste similaire :

bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0d_tvshows < [script].sql
Commandes Docker utiles
Lister les conteneurs actifs :

bash
Copier
Modifier
docker ps
Lister tous les conteneurs (y compris stoppés) :

bash
Copier
Modifier
docker ps -a
Démarrer un conteneur arrêté :

bash
Copier
Modifier
docker start <nom_du_conteneur>
(Ici : docker start mysql_project)

Arrêter un conteneur actif :

bash
Copier
Modifier
docker stop <nom_du_conteneur>
Se connecter au conteneur et exécuter bash (ou un autre shell) :

bash
Copier
Modifier
docker exec -it <nom_du_conteneur> bash
Se connecter à MySQL dans le conteneur (mode interactif) :

bash
Copier
Modifier
docker exec -it <nom_du_conteneur> mysql -uroot -p
(Mot de passe : root)

Exécuter un script SQL sans lancer la console interactive :

bash
Copier
Modifier
docker exec -i <nom_du_conteneur> mysql -uroot -p'root' < <script>.sql
(Ou en spécifiant la base : mysql -uroot -p'root' hbtn_0c_0 < 4-first_table.sql)

Afficher les logs du conteneur (utile si MySQL ne démarre pas) :

bash
Copier
Modifier
docker logs <nom_du_conteneur>
Conclusion
Ce projet illustre la manipulation de bases de données MySQL au sein d’un conteneur Docker. Il couvre des opérations de base (création, suppression, insertion, jointures) et des cas plus avancés comme la gestion de clés étrangères et de jointures multiples.

Pour toute question ou amélioration, n’hésite pas à créer une issue ou à proposer un pull request sur ce dépôt. Bonne continuation !