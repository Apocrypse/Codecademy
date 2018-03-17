SELECT name,
       CASE WHEN genre = 'romance' THEN 'fun'
            WHEN genre = 'comedy' THEN 'fun'
            ELSE 'serious'
       END AS 'mood'
FROM movies;
