-- * Data Processing at Scale: Movie Recommendation Database
-- * @author  : Kiruthika Ponnan - ASUID: 1227400293

-- Creating the Users table
CREATE TABLE users (
    userid SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Creating the Movies table
CREATE TABLE movies (
    movieid SERIAL PRIMARY KEY,
    title TEXT NOT NULL
);

-- Creating the Genres table
CREATE TABLE genres (
    genreid SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- Creating the Movie Genres (hasagenre) table
CREATE TABLE hasagenre (
    movieid INT REFERENCES movies(movieid),
    genreid INT REFERENCES genres(genreid),
    PRIMARY KEY (movieid, genreid)
);

-- Creating the Taginfo table
CREATE TABLE taginfo (
    tagid SERIAL PRIMARY KEY,
    content TEXT NOT NULL
);

-- Creating the Ratings table
CREATE TABLE ratings (
    userid INT REFERENCES users(userid),
    movieid INT REFERENCES movies(movieid),
    rating NUMERIC CHECK (rating >= 0 AND rating <= 5),
    timestamp BIGINT NOT NULL,
    PRIMARY KEY (userid, movieid)
);

-- Creating the Tags table
CREATE TABLE tags (
    userid INT REFERENCES users(userid),
    movieid INT REFERENCES movies(movieid),
    tagid INT REFERENCES taginfo(tagid),
    timestamp BIGINT NOT NULL,
    PRIMARY KEY (userid, movieid, tagid)
);


-- Copying the data from the dat files into the tables (for local use)
COPY users from '/home/users.dat' DELIMITER '%' CSV;
COPY movies from '/home/movies.dat' DELIMITER '%' CSV;
COPY genres from '/home/genres.dat' DELIMITER '%' CSV;
COPY hasagenre from '/home/hasagenre.dat' DELIMITER '%' CSV;
COPY taginfo from '/home/taginfo.dat' DELIMITER '%' CSV;
COPY ratings from '/home/ratings.dat' DELIMITER '%' CSV;
COPY tags from '/home/tags.dat' DELIMITER '%' CSV;

-- -- Drop the tables (for local use)
-- DROP TABLE tags;
-- DROP TABLE ratings;
-- DROP TABLE taginfo;
-- DROP TABLE hasagenre;
-- DROP TABLE genres;
-- DROP TABLE movies;
-- DROP TABLE users;
