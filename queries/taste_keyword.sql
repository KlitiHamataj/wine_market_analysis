SELECT
    wines.name AS wine_name,
    keywords_wine.group_name,
    COUNT(DISTINCT keywords.name) as keyword_count
FROM wines
JOIN keywords_wine ON keywords_wine.wine_id = wines.id
JOIN keywords ON keywords.id = keywords_wine.keyword_id
WHERE keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
AND keywords_wine.count > 10
GROUP BY wines.id, wines.name
HAVING COUNT(DISTINCT keywords.name) = 5;