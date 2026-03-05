-- Ce script affiche le nombre d'enregistrements pour chaque score dans la table 'second_table'.
-- Les résultats sont groupés par 'score', et le nombre de répétitions est nommé 'number'.
-- La liste est triée par le nombre d'occurrences (la colonne 'number') de manière décroissante.
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
