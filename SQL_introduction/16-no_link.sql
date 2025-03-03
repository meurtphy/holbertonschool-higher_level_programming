-- Liste tous les enregistrements de second_table avec un nom non vide
-- Affiche score et name, triés par score décroissant
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name != '' 
ORDER BY score DESC;
