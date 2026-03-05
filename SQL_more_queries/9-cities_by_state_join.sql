-- Ce script liste toutes les villes présentes dans la base avec le nom de leur état respectif.
-- On sélectionne l'ID et le nom de la ville, ainsi que le nom de l'état correspondant.
-- La jointure (JOIN) relie 'cities' et 'states' en faisant correspondre 'state_id' et 'id'.
-- Les résultats sont triés par l'ID de la ville dans l'ordre croissant (ASC).
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
