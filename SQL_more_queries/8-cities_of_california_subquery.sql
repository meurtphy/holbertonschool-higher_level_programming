-- Sélectionne les villes de l'État "California" en utilisant une sous-requête
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
