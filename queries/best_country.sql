SELECT
    countries.name AS country_name,
    countries.users_count,
    countries.wines_count,
    ROUND(AVG(wines.ratings_average), 2) AS avg_rating
FROM countries
JOIN regions ON regions.country_code = countries.code
JOIN wines ON wines.region_id = regions.id
GROUP BY country_name
ORDER BY avg_rating DESC
LIMIT 10;