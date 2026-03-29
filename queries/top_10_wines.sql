SELECT
    wines.name AS wine_name,
    ratings_average,
    ratings_count,
    countries.name AS country_name
FROM wines
JOIN regions ON wines.region_id = regions.id
JOIN countries ON regions.country_code = countries.code
WHERE ratings_count >= 1000
ORDER BY ratings_average DESC, ratings_count DESC -- if two wines have the same rating, prefer the one with mnore num of ratings
LIMIT 10