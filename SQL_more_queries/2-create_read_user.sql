-- Ce script prépare un environnement spécifique pour un utilisateur restreint.
-- 1. On crée la base de données 'hbtn_0d_2' si elle n'existe pas encore.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- 2. On crée l'utilisateur 'user_0d_2' sur l'hôte local (localhost).
--    Le mot de passe est défini comme 'user_0d_2_pwd'.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- 3. On accorde UNIQUEMENT le privilège de lecture (SELECT) à cet utilisateur.
--    Ce droit ne s'applique QUE sur la base 'hbtn_0d_2' et toutes ses tables (.*).
--    L'utilisateur ne pourra ni modifier, ni supprimer, ni créer de données.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- 4. On rafraîchit les privilèges pour que MySQL prenne en compte les nouveaux droits.
FLUSH PRIVILEGES;
