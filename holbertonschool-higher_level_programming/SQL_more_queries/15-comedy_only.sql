-- Ce script liste tous les titres de séries TV qui appartiennent au genre 'Comedy'.
-- 1. On part de la table 'tv_shows' pour obtenir les titres.
-- 2. Premier JOIN : On passe par la table de liaison 'tv_show_genres' via 'show_id'.
-- 3. Deuxième JOIN : On atteint la table 'tv_genres' via 'genre_id' pour filtrer par nom.
-- 4. WHERE : On restreint les résultats uniquement au genre 'Comedy'.
-- 5. ORDER BY : On trie les titres des séries par ordre alphabétique (A-Z).
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
