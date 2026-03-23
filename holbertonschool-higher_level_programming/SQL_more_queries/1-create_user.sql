-- Ce script crée un nouvel utilisateur nommé 'user_0d_1' sur le serveur MySQL.
-- L'utilisateur est restreint aux connexions provenant de 'localhost' (la machine locale).
-- Le mot de passe est défini par la clause 'IDENTIFIED BY'.
-- La clause 'IF NOT EXISTS' évite une erreur si l'utilisateur a déjà été créé.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- On accorde à cet utilisateur TOUS les privilèges sur TOUTES les bases de données (*.*).
-- 'WITH GRANT OPTION' permet à cet utilisateur de donner ses propres permissions à d'autres.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
-- Cette commande force MySQL à recharger les tables de droits pour appliquer les changements immédiatement.
FLUSH PRIVILEGES;
