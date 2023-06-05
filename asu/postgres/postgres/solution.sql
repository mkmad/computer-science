--------------------------------------------------------------------

-- * Data Processing at Scale: Movie Recommendation Database
-- * @author  : Kiruthika Ponnan - ASUID: 1227400293
-- ASSIGNMENT 2

--------------------------------------------------------------------


-- Write a SQL query to return the total number of movies for each genre.
CREATE TABLE query1 AS
SELECT genres.name AS name, COUNT(movieid) AS moviecount
FROM genres JOIN hasagenre
ON hasagenre.genreid = genres.genreid
GROUP BY genres.name;


-- Write a SQL query to return the average rating for each genre.
CREATE TABLE query2 AS
SELECT g.name AS name, AVG(r.rating) AS rating
FROM genres g
LEFT JOIN hasagenre h ON g.genreid = h.genreid
LEFT JOIN ratings r ON h.movieid = r.movieid
GROUP BY g.name;


-- Write a SQL query to return the title and number of ratings for each 
-- movie that has at least 10 ratings.
CREATE TABLE query3 AS
SELECT m.title AS title, COUNT(r.rating) AS CountOfRatings
FROM movies m
JOIN ratings r ON m.movieid = r.movieid
GROUP BY m.movieid, m.title
HAVING COUNT(r.rating) >= 10;


-- Write a SQL query to return the title of each movie that is a comedy.
CREATE TABLE query4 AS
SELECT m.movieid AS movieid, m.title AS title
FROM movies m
JOIN hasagenre h ON m.movieid = h.movieid
JOIN genres g ON h.genreid = g.genreid
WHERE g.name = 'Comedy';


-- Write a SQL query to return the title and average rating of each movie
CREATE TABLE query5 AS
SELECT m.title AS title, AVG(r.rating) AS average
FROM movies m
JOIN ratings r ON m.movieid = r.movieid
GROUP BY m.movieid, m.title;


-- Write a SQL query to return the average rating of all movies that are
-- comedies.
CREATE TABLE query6 AS
SELECT AVG(r.rating) AS average
FROM movies m
JOIN hasagenre h ON m.movieid = h.movieid
JOIN genres g ON h.genreid = g.genreid
JOIN ratings r ON m.movieid = r.movieid
WHERE g.name = 'Comedy';


-- Write a SQL query to return the average rating of all movies that are 
-- comedies or romances.
CREATE TABLE query7 AS
SELECT AVG(r.rating) AS average
FROM ratings r, movies m
WHERE r.movieid = m.movieid
AND m.movieid IN (
    SELECT hg.movieid
    FROM hasagenre hg, genres g
    WHERE hg.genreid = g.genreid
    AND g.name='Comedy'
    INTERSECT
    SELECT hg.movieid
    FROM hasagenre hg, genres g
    WHERE hg.genreid = g.genreid
    AND g.name='Romance'
);


-- Write a SQL query to return the average rating of all movies that are
-- romances but not comedies.
CREATE TABLE query8 AS
SELECT AVG(r.rating) AS average
FROM ratings r, movies m
WHERE r.movieid = m.movieid
AND m.movieid IN (
    SELECT hg.movieid
    FROM hasagenre hg, genres g
    WHERE hg.genreid = g.genreid
    AND g.name='Romance'
    EXCEPT
    SELECT hg.movieid
    FROM hasagenre hg, genres g
    WHERE hg.genreid = g.genreid
    AND g.name='Comedy'
);


-- Write a SQL query to return the movieid and rating of all ratings where
-- the userid is supplied to the query.
CREATE TABLE query9 AS
SELECT r.movieid AS movieid, r.rating AS rating
FROM ratings r
WHERE r.userid = :v1;

-- -- Printing all the tables (for testing purposes only)
-- SELECT * FROM query1;
-- SELECT * FROM query2;
-- SELECT * FROM query3;
-- SELECT * FROM query4;
-- SELECT * FROM query5;
-- SELECT * FROM query6;
-- SELECT * FROM query7;
-- SELECT * FROM query8;
-- SELECT * FROM query9;

-- -- Dropping all the tables (for testing purposes only)
-- DROP TABLE query1;
-- DROP TABLE query2;
-- DROP TABLE query3;
-- DROP TABLE query4;
-- DROP TABLE query5;
-- DROP TABLE query6;
-- DROP TABLE query7;
-- DROP TABLE query8;
-- DROP TABLE query9;
