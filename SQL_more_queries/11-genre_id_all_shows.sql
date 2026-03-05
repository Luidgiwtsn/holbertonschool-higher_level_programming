-- Ce script liste toutes les séries (tv_shows) et leurs identifiants de genre associés.
-- On utilise un 'LEFT JOIN' pour inclure toutes les séries, même celles qui n'ont pas de genre.
-- Si une série n'a pas de genre, la colonne 'genre_id' affichera NULL.
-- Les résultats sont triés par titre de série et par identifiant de genre (ordre croissant).
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
