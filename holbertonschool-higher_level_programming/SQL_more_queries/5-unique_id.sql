-- Ce script crée la table 'unique_id' dans la base de données actuelle.
-- La colonne 'id' est un entier (INT) avec une valeur par défaut de 1.
-- La contrainte 'UNIQUE' garantit que chaque 'id' présent dans la table est différent.
-- La colonne 'name' peut contenir jusqu'à 256 caractères.
-- Si tu essaies d'insérer deux lignes avec le même 'id', MySQL bloquera la deuxième insertion.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
