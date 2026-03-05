-- Ce script liste toutes les séries (tv_shows) qui possèdent au moins un genre associé.
-- L'utilisation de 'JOIN' (équivalent à 'INNER JOIN') exclut les séries sans genre.
-- On récupère le titre de la série et l'ID du genre correspondant.
-- Les résultats sont triés par titre (A-Z) puis par ID de genre (ordre croissant).
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
