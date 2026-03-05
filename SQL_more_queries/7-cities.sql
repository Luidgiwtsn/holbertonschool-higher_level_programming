-- Ce script crée la base 'hbtn_0d_usa' et la table 'cities' avec une relation vers 'states'.
-- 1. Création de la base de données si elle n'existe pas.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- 2. Sélection de la base pour les opérations suivantes.
USE hbtn_0d_usa;
-- 3. Création de la table 'cities' :
--    - 'id' : Identifiant unique auto-incrémenté et clé primaire.
--    - 'state_id' : Référence l'ID de l'état auquel la ville appartient.
--    - 'name' : Nom de la ville (ne peut pas être vide).
--    - 'FOREIGN KEY' : Lie 'state_id' à la colonne 'id' de la table 'states'.
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
