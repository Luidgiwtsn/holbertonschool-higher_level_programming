-- Ce script modifie une valeur existante dans la table 'second_table'.
-- Il met à jour le score de l'enregistrement où le nom est 'Bob' pour le passer à 10.
-- La clause 'WHERE' est cruciale : sans elle, TOUS les scores de la table seraient modifiés.
UPDATE second_table SET score = 10 WHERE name = 'Bob';
