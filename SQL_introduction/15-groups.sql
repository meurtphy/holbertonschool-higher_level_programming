-- Compte le nombre d'enregistrements ayant le même score dans second_table
-- Affiche score et le nombre d'occurrences (alias "number"), trié en ordre décroissant
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
