📌 Étape 1 : Vérifier que la table users a bien été créée
Connecte-toi à MySQL :

bash
Copier
Modifier
docker exec -it mysql_project mysql -uroot -p
Puis, dans MySQL (mysql>), exécute :

sql
Copier
Modifier
USE hbtn_0c_0;
SHOW TABLES;
✅ Si tout fonctionne, tu devrais voir users apparaître dans la liste des tables.

📌 Étape 2 : Vérifier la structure de la table
Toujours dans MySQL (mysql>), exécute :

sql
Copier
Modifier
DESCRIBE users;
Cela affichera la structure de la table users (colonnes, types de données, clés, etc.).

📌 Étape 3 : Insérer et lire des données (facultatif)
Si tu veux tester la table en insérant des données :

sql
Copier
Modifier
INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');
SELECT * FROM users;
✅ Tu devrais voir les 3 utilisateurs insérés.

