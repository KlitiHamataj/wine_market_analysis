SELECT
    vintages.year AS vintage_year,
    ROUND(AVG(wines.ratings_average), 2) AS avg_rating
FROM vintages
JOIN wines ON wines.id = vintages.wine_id
GROUP BY vintage_year
ORDER BY vintage_year ASC;