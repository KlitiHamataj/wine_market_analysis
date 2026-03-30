-- Top 5 Cabernet Sauvignon
SELECT * FROM (
    SELECT wines.name AS wine_name, ratings_average, ratings_count, 'Cabernet Sauvignon' AS grape
    FROM wines
    WHERE wines.name LIKE '%Cabernet Sauvignon%'
    AND ratings_count > 50
    ORDER BY ratings_average DESC
    LIMIT 5
)

UNION ALL
-- Top 5 Merlot
SELECT * FROM (
    SELECT wines.name AS wine_name, ratings_average, ratings_count, 'Merlot' AS grape
    FROM wines
    WHERE wines.name LIKE '%Merlot%'
    AND ratings_count > 50
    ORDER BY ratings_average DESC
    LIMIT 5
)

UNION ALL
-- Top 5 Chardonnay
SELECT * FROM (
    SELECT wines.name AS wine_name, ratings_average, ratings_count, 'Chardonnay' AS grape
    FROM wines
    WHERE wines.name LIKE '%Chardonnay%'
    AND ratings_count > 50
    ORDER BY ratings_average DESC
    LIMIT 5
);