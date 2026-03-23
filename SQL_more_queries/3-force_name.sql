-- Ce script crée la table 'force_name' dans la base de données actuelle.
-- La table possède deux colonnes : 'id' (Entier) et 'name' (Chaîne de caractères).
-- La contrainte 'NOT NULL' sur la colonne 'name' signifie qu'il est impossible 
-- d'insérer une ligne sans donner un nom.
-- La clause 'IF NOT EXISTS' évite une erreur si la table est déjà présente.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
