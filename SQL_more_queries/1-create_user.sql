-- Crée l'utilisateur 'user_0d_1' avec le mot de passe 'user_0d_1_pwd' s'il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorde tous les privilèges à 'user_0d_1' sur tout le serveur MySQL
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Applique les changements
FLUSH PRIVILEGES;
