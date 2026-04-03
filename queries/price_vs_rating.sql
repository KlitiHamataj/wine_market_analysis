SELECT
    name,
    price_euros,
    ratings_average
FROM vintages
WHERE price_euros IS NOT NULL
AND ratings_average IS NOT NULL
AND ratings_average > 0