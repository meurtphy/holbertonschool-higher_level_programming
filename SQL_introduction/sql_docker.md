Projet SQL – Introduction à MySQL
Ce projet a pour objectif de vous familiariser avec la manipulation de bases de données MySQL à l’aide de scripts SQL. Chaque script correspond à un exercice spécifique. L’ensemble est exécuté dans un conteneur Docker pour garantir un environnement propre et isolé.

Note : Tous les scripts sont testés sur MySQL 8.0 dans un conteneur Docker nommé mysql_project avec le mot de passe root.

Table des matières
Prérequis et Installation
Exercices
0. Liste des bases de données
Création d’une base de données
Suppression d’une base de données
Liste des tables
Création de la table first_table
Description complète de first_table
Liste de toutes les lignes de first_table
Insertion dans first_table
Compter les enregistrements avec id = 89
Création complète de second_table
Liste des enregistrements par score décroissant
Sélection des enregistrements avec score >= 10
Mise à jour du score de “Bob”
Suppression des enregistrements avec score <= 5
Moyenne des scores
Nombre d’enregistrements par score
Liste des enregistrements avec nom non vide
Commandes d’Exécution Générales
Conclusion
Prérequis et Installation
Docker doit être installé sur votre machine.

Pour lancer le conteneur MySQL, exécutez :

bash
Copier
Modifier
docker run --name mysql_project \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=mydatabase \
    -p 3306:3306 \
    -d mysql:8.0
Pour vous connecter à MySQL dans le conteneur :
bash
Copier
Modifier
docker exec -it mysql_project mysql -uroot -p
Entrez alors le mot de passe root.

Exercices
0. Liste des bases de données
Fichier : 0-list_databases.sql
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


1. Création d’une base de données
Fichier : 1-create_database_if_missing.sql
Contenu :
sql
Copier
Modifier
-- Crée la base de données hbtn_0c_0 si elle n’existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' < 1-create_database_if_missing.sql

2. Suppression d’une base de données
Fichier : 2-remove_database.sql
Contenu :
sql
Copier
Modifier
-- Supprime la base de données hbtn_0c_0 si elle existe
DROP DATABASE IF EXISTS hbtn_0c_0;
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' < 2-remove_database.sql

3. Liste des tables
Fichier : 3-list_tables.sql
Contenu :
sql
Copier
Modifier
SHOW TABLES;
Exécution (exemple sur la base mysql) :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' mysql < 3-list_tables.sql

4. Création de la table first_table
Fichier : 4-first_table.sql
Contenu :
sql
Copier
Modifier
-- Crée la table first_table si elle n’existe pas
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 4-first_table.sql

5. Description complète de first_table
Fichier : 5-full_table.sql
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

6. Liste de toutes les lignes de first_table
Fichier : 6-list_values.sql
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

7. Insertion dans first_table
Fichier : 7-insert_value.sql
Contenu :
sql
Copier
Modifier
-- Insère une nouvelle ligne dans la table first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
Exécution :
bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 7-insert_value.sql

8. Compter les enregistrements avec id = 89
Fichier : 8-count_89.sql
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
Pour n’afficher que le résultat final, redirigez la sortie via tail -1.


9. Création complète de second_table
Fichier : 9-full_creation.sql
Contenu :
sql
Copier
Modifier
-- Crée la table second_table si elle n’existe pas
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insère les enregistrements
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

10. Liste des enregistrements par score décroissant
Fichier : 10-top_score.sql
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

11. Sélection des enregistrements avec score >= 10
Fichier : 11-best_score.sql
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

12. Mise à jour du score de “Bob”
Fichier : 12-no_cheating.sql
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

13. Suppression des enregistrements avec score <= 5
Fichier : 13-change_class.sql
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

14. Moyenne des scores
Fichier : 14-average.sql
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

15. Nombre d’enregistrements par score
Fichier : 15-groups.sql
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

16. Liste des enregistrements avec nom non vide
Fichier : 16-no_link.sql
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
Commandes d’Exécution Générales
Pour exécuter un script SQL dans le conteneur (remplacez [fichier].sql et [base] si besoin) :

bash
Copier
Modifier
docker exec -i mysql_project mysql -uroot -p'root' [base] < [fichier].sql
Pour lancer une session interactive MySQL :

bash
Copier
Modifier
docker exec -it mysql_project mysql -uroot -p

Conclusion

Ce projet vous permet de :

Créer et supprimer des bases de données

Créer et manipuler des tables (insertion, sélection, mise à jour, suppression)

Utiliser des fonctions SQL telles que AVG, COUNT et des clauses de regroupement

Exécuter des scripts SQL dans un environnement Docker isolé

Chaque fichier SQL remplit un objectif précis pour mieux comprendre la manipulation de bases de données avec MySQL.