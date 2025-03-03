Projet SQL – Holberton School – SQL_introduction
Ce projet a pour but de manipuler des bases de données MySQL en utilisant des scripts SQL. Tous les scripts sont testés dans un environnement Docker sur un serveur MySQL (version 8.0).
Les fichiers SQL sont organisés dans le répertoire SQL_introduction et chaque fichier correspond à un exercice spécifique.

Table des matières
0. List databases
1. Create a database
2. Delete a database
3. List tables
4. First table
5. Full description
6. List all in table
7. First add
8. Count 89
9. Full creation
10. List by best
11. Select the best
12. Cheating is bad
13. Score too low
14. Average
15. Number by score
16. Say my name
Prérequis
Docker doit être installé sur votre machine.
Un conteneur MySQL (version 8.0) est utilisé pour exécuter les scripts.
Les commandes d'exécution se font à partir du terminal.
Démarrer le conteneur MySQL
Pour lancer le conteneur, utilisez la commande suivante :

bash
Copier
docker run --name mysql_project -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=mydatabase -p 3306:3306 -d mysql:8.0
Pour se connecter à MySQL dans le conteneur :

bash
Copier
docker exec -it mysql_project mysql -uroot -p
(Le mot de passe est root.)

Exercice 0 – List databases
Fichier : 0-list_databases.sql

But : Afficher la liste de toutes les bases de données du serveur.

Contenu :

sql
Copier
SHOW DATABASES;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' < 0-list_databases.sql
Exercice 1 – Create a database
Fichier : 1-create_database_if_missing.sql

But : Créer la base de données hbtn_0c_0 si elle n'existe pas.
Remarque : Vous n'êtes pas autorisé à utiliser SELECT ou SHOW.

Contenu :

sql
Copier
-- Crée la base de données hbtn_0c_0 si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' < 1-create_database_if_missing.sql
Exercice 2 – Delete a database
Fichier : 2-remove_database.sql

But : Supprimer la base de données hbtn_0c_0 si elle existe.
Remarque : Vous n'êtes pas autorisé à utiliser SELECT ou SHOW.

Contenu :

sql
Copier
-- Supprime la base de données hbtn_0c_0 si elle existe
DROP DATABASE IF EXISTS hbtn_0c_0;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' < 2-remove_database.sql
Exercice 3 – List tables
Fichier : 3-list_tables.sql

But : Lister toutes les tables d'une base de données donnée.
Le nom de la base est passé en argument.

Contenu :

sql
Copier
SHOW TABLES;
Exécution (exemple avec la base mysql) :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' mysql < 3-list_tables.sql
Exercice 4 – First table
Fichier : 4-first_table.sql

But : Créer une table appelée first_table dans la base hbtn_0c_0.
Description :

id de type INT
name de type VARCHAR(256)
Si la table existe déjà, le script ne doit pas échouer.
Contenu :

sql
Copier
-- Crée la table first_table si elle n'existe pas
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 4-first_table.sql
Exercice 5 – Full description
Fichier : 5-full_table.sql

But : Afficher la description complète de la table first_table (structure de création).
Remarque : Vous n'êtes pas autorisé à utiliser DESCRIBE ou EXPLAIN.

Contenu :

sql
Copier
SHOW CREATE TABLE first_table;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 5-full_table.sql
Exercice 6 – List all in table
Fichier : 6-list_values.sql

But : Lister toutes les lignes de la table first_table dans la base hbtn_0c_0.
Tous les champs doivent être affichés.

Contenu :

sql
Copier
SELECT * FROM first_table;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 6-list_values.sql
Exercice 7 – First add
Fichier : 7-insert_value.sql

But : Insérer une nouvelle ligne dans la table first_table avec les valeurs suivantes :

id = 89
name = "Best School"
Contenu :

sql
Copier
-- Insère une nouvelle ligne dans la table first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 7-insert_value.sql
Exercice 8 – Count 89
Fichier : 8-count_89.sql

But : Afficher le nombre d'enregistrements avec id = 89 dans la table first_table.
La colonne résultante doit s'appeler average n'est pas demandée ici, mais l'exercice veut juste compter les occurrences.

Contenu :

sql
Copier
SELECT COUNT(*) FROM first_table WHERE id = 89;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 8-count_89.sql
(Pour afficher uniquement le résultat final, vous pouvez utiliser | tail -1 après la commande.)

Exercice 9 – Full creation
Fichier : 9-full_creation.sql

But : Créer une table second_table dans la base hbtn_0c_0 et y insérer plusieurs lignes.
Description de la table :

id INT
name VARCHAR(256)
score INT
Enregistrements à insérer :
(1, 'John', 10)
(2, 'Alex', 3)
(3, 'Bob', 14)
(4, 'George', 8)
Contenu :

sql
Copier
-- Crée la table second_table si elle n'existe pas
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
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 9-full_creation.sql
Exercice 10 – List by best
Fichier : 10-top_score.sql

But : Lister tous les enregistrements de la table second_table en affichant le score et le nom (dans cet ordre), triés par score décroissant.

Contenu :

sql
Copier
SELECT score, name FROM second_table ORDER BY score DESC;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 10-top_score.sql
Exercice 11 – Select the best
Fichier : 11-best_score.sql

But : Lister tous les enregistrements de la table second_table ayant un score >= 10, affichant le score et le nom, triés par score décroissant.

Contenu :

sql
Copier
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 11-best_score.sql
Exercice 12 – Cheating is bad
Fichier : 12-no_cheating.sql

But : Mettre à jour le score de Bob à 10 dans la table second_table.
Remarque : On ne doit utiliser que le champ name pour identifier Bob.

Contenu :

sql
Copier
UPDATE second_table SET score = 10 WHERE name = 'Bob';
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 12-no_cheating.sql
Exercice 13 – Score too low
Fichier : 13-change_class.sql

But : Supprimer tous les enregistrements de second_table ayant un score <= 5.

Contenu :

sql
Copier
DELETE FROM second_table WHERE score <= 5;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 13-change_class.sql
Exercice 14 – Average
Fichier : 14-average.sql

But : Calculer la moyenne des scores de tous les enregistrements de la table second_table.
La colonne résultat doit s'appeler average.

Contenu :

sql
Copier
SELECT AVG(score) AS average FROM second_table;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 14-average.sql
Exercice 15 – Number by score
Fichier : 15-groups.sql

But : Lister le nombre d'enregistrements pour chaque score dans la table second_table.
Le résultat doit afficher le score et le nombre d'enregistrements sous l'étiquette number.
Les résultats doivent être triés par le nombre d'enregistrements en ordre décroissant.

Contenu :

sql
Copier
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 15-groups.sql
Exercice 16 – Say my name
Fichier : 16-no_link.sql

But : Lister tous les enregistrements de la table second_table dont le champ name n'est pas vide.
Les résultats doivent afficher le score et le nom (dans cet ordre) et être triés par score décroissant.

Contenu :

sql
Copier
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
Exécution :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 16-no_link.sql
Commandes d'exécution générales
Pour exécuter un script SQL sur le conteneur, utilisez la commande :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' [nom_de_la_base] < [nom_du_fichier].sql
Exemple pour la base hbtn_0c_0 :

bash
Copier
docker exec -i mysql_project mysql -uroot -p'root' hbtn_0c_0 < 9-full_creation.sql
Pour vérifier les modifications ou la structure, vous pouvez vous connecter en mode interactif :

bash
Copier
docker exec -it mysql_project mysql -uroot -p
Conclusion
Ce README récapitule l'ensemble des commandes SQL demandées pour ce projet. Chaque fichier a un rôle précis, de la création et suppression de bases de données à la manipulation de tables et données.
Ce projet vous permet de vous familiariser avec les commandes SQL essentielles et leur exécution dans un environnement Docker isolé.
