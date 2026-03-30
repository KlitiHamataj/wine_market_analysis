SELECT
    wines.winery_id,
    COUNT(wines.id) AS wine_count,
    ROUND(AVG(wines.ratings_average), 2) AS avg_rating
FROM wines
GROUP BY wines.winery_id
HAVING wine_count >= 5
ORDER BY avg_rating DESC
LIMIT 3;