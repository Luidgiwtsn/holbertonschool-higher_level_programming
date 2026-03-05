-- Ce script affiche tous les genres de la base 'hbtn_0d_tvshows' et le nombre de séries associées.
-- 1. On sélectionne le nom du genre (renommé 'genre' pour l'affichage).
-- 2. On compte le nombre d'occurrences de chaque 'genre_id' dans la table de liaison.
-- 3. 'JOIN' relie les genres aux séries (seuls les genres avec au moins une série sont affichés).
-- 4. 'GROUP BY' rassemble les résultats par nom de genre.
-- 5. 'ORDER BY' trie la liste par le nombre de séries, du plus grand au plus petit.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
