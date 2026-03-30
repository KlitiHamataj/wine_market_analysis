SELECT
    wines.winery_id,
    COUNT(DISTINCT regions.id) AS region_count
FROM wines
JOIN regions ON wines.region_id = regions.id
GROUP BY wines.winery_id
ORDER BY region_count DESC
LIMIT 3;