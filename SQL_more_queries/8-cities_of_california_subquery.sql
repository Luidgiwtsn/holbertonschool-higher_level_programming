-- Ce script liste toutes les villes de l'État de Californie présentes dans la base.
-- 1. La sous-requête entre parenthèses cherche d'abord l'ID correspondant au nom 'California' dans la table 'states'.
-- 2. La requête principale utilise cet ID pour filtrer les lignes de la table 'cities'.
-- 3. Les résultats (id et name) sont triés par ID de ville dans l'ordre croissant.
SELECT id, name 
FROM cities 
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
) 
ORDER BY id ASC;
