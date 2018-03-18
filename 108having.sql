SELECT price, ROUND(AVG(downloads))
FROM fake_apps
GROUP BY price
HAVING COUNT(*) > 9;
