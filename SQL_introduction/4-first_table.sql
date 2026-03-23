-- Ce script crée une table appelée 'first_table' dans la base de données actuelle.
-- La table possède deux colonnes : 'id' (Entier) et 'name' (Chaîne de caractères jusqu'à 256 caractères).
-- La clause 'IF NOT EXISTS' permet d'éviter les erreurs si la table est déjà présente.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
