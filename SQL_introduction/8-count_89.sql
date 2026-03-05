-- Ce script compte le nombre d'enregistrements (lignes) dans 'first_table'
-- qui possèdent un 'id' égal à 89.
-- COUNT(*) est une fonction d'agrégation qui calcule le total des lignes correspondant au filtre.
SELECT COUNT(*) FROM first_table WHERE id = 89;
