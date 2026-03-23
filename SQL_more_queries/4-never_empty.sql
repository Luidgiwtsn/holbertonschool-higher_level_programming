-- Ce script crée la table 'id_not_null' dans la base de données actuelle.
-- La colonne 'id' est un entier (INT) avec une valeur par défaut de 1.
-- La colonne 'name' peut contenir jusqu'à 256 caractères.
-- Si tu insères une ligne sans préciser l'id, MySQL lui attribuera automatiquement 1.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
