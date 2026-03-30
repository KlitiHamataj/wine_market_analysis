-- SELECT name FROM wines LIMIT 10

-- SELECT COUNT(*) FROM wines

-- PRAGMA table_info(wines);

-- PRAGMA table_info(regions);

-- PRAGMA table_info(countries);

--SELECT COUNT(*) FROM wineries;

-- SELECT COUNT(DISTINCT winery_id) FROM wines;

-- What winery_ids exist in wines?
--SELECT DISTINCT winery_id FROM wines LIMIT 10;

-- What ids exist in wineries?
-- SELECT id FROM wineries LIMIT 10;

/* SELECT
    wines.winery_id,
    COUNT(wines.id) AS wine_count,
    AVG(wines.ratings_average) AS avg_rating
FROM wines
GROUP BY wines.winery_id
HAVING wine_count >= 5
ORDER BY avg_rating DESC
LIMIT 10; */

-- SELECT name FROM vintages LIMIT 10;

/* SELECT DISTINCT winery_id, name
FROM wines
LIMIT 10; */

/*SELECT name FROM vintages
WHERE wine_id IN (
    SELECT id FROM wines WHERE winery_id = 1252
)
LIMIT 5;*/

/*SELECT
    wines.winery_id,
    COUNT(DISTINCT regions.id) AS region_count
FROM wines
JOIN regions ON wines.region_id = regions.id
GROUP BY wines.winery_id
ORDER BY region_count DESC
LIMIT 3;*/

/*SELECT
    wines.winery_id,
    COUNT(wines.id) AS wine_count
FROM wines
GROUP BY wines.winery_id
ORDER BY wine_count DESC
LIMIT 3;*/

/*SELECT
    keywords.name,
    COUNT(*) as wine_count
FROM keywords
JOIN keywords_wine ON keywords.id = keywords_wine.keyword_id
WHERE keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
AND keywords_wine.count > 10
GROUP BY keywords.name;*/

/*SELECT
    wines.name AS wine_name,
    keywords_wine.group_name,
    COUNT(DISTINCT keywords.name) as keyword_count
FROM wines
JOIN keywords_wine ON keywords_wine.wine_id = wines.id
JOIN keywords ON keywords.id = keywords_wine.keyword_id
WHERE keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
AND keywords_wine.count > 10
GROUP BY wines.id, wines.name
HAVING COUNT(DISTINCT keywords.name) = 5;*/

-- PRAGMA table_info(grapes)

-- PRAGMA table_info(most_used_grapes_per_country);

/*SELECT
    grapes.name AS grape_name,
    SUM(most_used_grapes_per_country.wines_count) total_wines
FROM grapes
JOIN most_used_grapes_per_country ON most_used_grapes_per_country.grape_id = grapes.id
GROUP BY grape_name
ORDER BY total_wines DESC
LIMIT 3;*/

/*SELECT wines.name, ratings_average, ratings_count
FROM wines
WHERE wines.name LIKE '%Chardonnay%'
AND ratings_count > 100
ORDER BY ratings_average DESC
LIMIT 5;*/

/*SELECT wines.name AS wine_name, ratings_average, ratings_count, 'Cabernet Sauvignon' AS grape
FROM wines
WHERE wines.name LIKE '%Cabernet Sauvignon%'
AND ratings_count > 100
ORDER BY ratings_average DESC
LIMIT 5*/

SELECT
    vintages.year AS vintage_year,
    ROUND(AVG(wines.ratings_average), 2) AS avg_rating
FROM vintages
JOIN wines ON wines.id = vintages.wine_id
GROUP BY vintage_year
ORDER BY avg_rating DESC
LIMIT 10;