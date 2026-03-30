SELECT
    grapes.name AS grape_name,
    SUM(most_used_grapes_per_country.wines_count) total_wines
FROM grapes
JOIN most_used_grapes_per_country ON most_used_grapes_per_country.grape_id = grapes.id
GROUP BY grape_name
ORDER BY total_wines DESC
LIMIT 3;