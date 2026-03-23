-- Ce script liste toutes les séries TV et leurs genres respectifs.
-- 1. On utilise un premier 'LEFT JOIN' pour inclure toutes les séries de 'tv_shows',
--    même si elles n'ont pas d'entrée dans la table de liaison 'tv_show_genres'.
-- 2. On utilise un second 'LEFT JOIN' pour récupérer le nom du genre dans 'tv_genres'.
-- 3. Si une série n'a pas de genre, la colonne 'name' affichera 'NULL'.
-- 4. Les résultats sont triés par titre de série (A-Z) puis par nom de genre (A-Z)
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
