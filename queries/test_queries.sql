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

/* SELECT name FROM vintages
WHERE wine_id IN (
    SELECT id FROM wines WHERE winery_id = 1235
)
LIMIT 5; */
