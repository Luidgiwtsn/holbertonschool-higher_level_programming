-- Ce script prépare la base de données 'hbtn_0d_usa' et crée la table 'states'.
-- 1. Création de la base de données si elle n'existe pas déjà.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- 2. Sélection de la base de données pour que les commandes suivantes s'y appliquent.
USE hbtn_0d_usa;
-- 3. Création de la table 'states' avec des contraintes d'intégrité fortes :
--    - 'id' : Entier unique, ne peut pas être vide, s'incrémente tout seul 
--             à chaque ajout et sert de clé primaire (identifiant unique).
--    - 'name' : Chaîne de caractères de 256 max, ne peut pas être vide.
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
