-- Ce script liste les scores et les noms de la table 'second_table' en filtrant les données vides.
-- On exclut les lignes où le nom est absent (NULL) ou simplement une chaîne vide ('').
-- Les résultats sont classés du score le plus élevé au plus bas.
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
