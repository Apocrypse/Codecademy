SELECT price, COUNT(*)
FROM fake_apps
WHERE downloads > 20000
GROUP BY price;
