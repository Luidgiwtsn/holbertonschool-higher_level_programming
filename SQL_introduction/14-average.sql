-- Ce script calcule la moyenne de tous les scores dans la table 'second_table'.
-- La fonction AVG() additionne tous les scores et divise par le nombre de lignes.
-- Le résultat est affiché sous le nom de colonne 'average' grâce à l'alias 'AS'.
SELECT AVG(score) AS average FROM second_table;
