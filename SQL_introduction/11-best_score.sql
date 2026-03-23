-- Ce script liste les enregistrements de 'second_table' ayant un score supérieur ou égal à 10.
-- Les résultats affichent les colonnes 'score' et 'name', dans cet ordre.
-- Les lignes sont triées par score décroissant (du plus grand au plus petit).
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
