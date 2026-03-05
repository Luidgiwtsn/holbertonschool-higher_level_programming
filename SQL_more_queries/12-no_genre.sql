-- Ce script liste toutes les séries (tv_shows) qui ne sont liées à aucun genre.
-- On utilise un 'LEFT JOIN' pour inclure toutes les séries, même celles sans genre.
-- La clause 'WHERE' filtre ensuite pour ne garder QUE les séries où l'ID du genre est absent (NULL).
-- Les résultats sont triés par titre de série (ordre croissant).
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
