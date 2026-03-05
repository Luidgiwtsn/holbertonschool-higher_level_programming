-- Ce script crée la table 'second_table' et y insère plusieurs lignes de données.
-- La table contient trois colonnes : 'id' (Entier), 'name' (Texte) et 'score' (Entier).
-- La clause 'IF NOT EXISTS' garantit que le script ne plante pas si la table est déjà là.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insertion de plusieurs enregistrements en une seule commande.
-- Chaque parenthèse représente une nouvelle ligne dans la table.
INSERT INTO second_table (id, name, score) VALUES 
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
