-- Ce script affiche tous les genres associés à la série 'Dexter'.
-- 1. On commence par la table 'tv_genres' pour obtenir les noms des genres.
-- 2. Premier JOIN : On relie les genres à la table de liaison 'tv_show_genres'.
-- 3. Deuxième JOIN : On relie cette table de liaison à 'tv_shows' pour accéder aux titres des séries.
-- 4. WHERE : On filtre précisément sur le titre 'Dexter'.
-- 5. ORDER BY : On trie les genres par ordre alphabétique.
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
