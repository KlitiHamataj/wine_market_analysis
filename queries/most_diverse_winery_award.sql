SELECT
    wines.winery_id,
    COUNT(wines.id) AS wine_count
FROM wines
GROUP BY wines.winery_id
ORDER BY wine_count DESC
LIMIT 3;