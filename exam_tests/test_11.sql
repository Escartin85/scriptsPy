/*
Consider a large movie database with the following schema:

TABLE movies
    id INTEGER NOT NULL PRIMARY KEY
    name VARCHAR(30) NOT NULL

TABLE visitors
    id INTEGER NOT NULL PRIMARY KEY
    name VARCHAR(30) NOT NULL

TABLE movies_visitors
    movieId INTEGER NOT NULL REFERENCES movies(id)
    visitorId INTEGER NOT NULL REFERENCES visitors(id)
    PRIMARY KEY (movieId, visitorId)


Select all queries that return movies having at least the average number of visitors
For example, if there are three movies A, B and C, with 1, 5 and 6 visitors, respectively, the average number
of visitors is (1 + 5 + 6)/3 = 4 and the query should return only movies B and C.

*1 - SELECT movieId, COUNT(*)
    FROM movies_visitors GROUP BY movieId HAVING COUNT(*) >=
      ((SELECT COUNT(*) FROM movies_visitors)*1.0/(SELECT COUNT(*) FROM movies));

2 - SELECT id, COUNT(*)
    FROM movies LEFT JOIN movies_visitors ON movieId = id
    GROUP BY id HAVING COUNT(*) >= AVG(COUNT(*));

*3 - SELECT id, COUNT(*)
    FROM movies JOIN movies_visitors ON movieId = id
    GROUP BY id WHERE COUNT(*) >=
      ((SELECT COUNT(*) FROM movies_visitors)*1.0/(SELECT COUNT(*) FROM movies));

4 - SELECT id, COUNT(*)
    FROM movies JOIN movies_visitors ON movieId = id
    GROUP BY id HAVING COUNT(*) >=
*/
