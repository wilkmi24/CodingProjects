CREATE DATABASE movies_db;

CREATE TABLE tbl_movies(
    movie_id INT PRIMARY KEY NOT NULL IDENTITY (1,1),
    movie_title VARCHAR(50) NOT NULL,
    movie_genre VARCHAR (50) NOT NULL
);

INSERT INTO tbl_movies
(movie_title, movie_genre)
VALUES
('black widow', 'action'),
('frozen', 'childrens'),
('singing in the rain', 'musical'),
('molly''s game', 'drama'),
('avengers', 'action')
;

SELECT * FROM tbl_movies

CREATE TABLE tbl_actors (
    actor_id INT PRIMARY KEY NOT NULL IDENTITY (100,1),
    actor_fname VARCHAR (50) NOT NULL,
    actor_lname VARCHAR(50) NOT NULL,
    actor_movie_id INT NOT NULL CONSTRAINT fk_movie_id FOREIGN KEY REFERENCES tbl_movies(movie_id) ON UPDATE CASCADE ON DELETE CASCADE
);


INSERT INTO tbl_actors
    (actor_fname, actor_lname, actor_movie_id)
    VALUES
    ('scarlett', 'johansson', 1),
    ('kristen', 'bell', 2),
    ('gene', 'kelly', 3),
    ('jessica', 'chastain', 4),
    ('scarlett', 'johansson', 1)
    ;

    SELECT * FROM tbl_movies;

    SELECT * FROM tbl_actors;

    SELECT tbl_movies.movie_title, tbl_movies.movie_genre, tbl_actors.actor_fname, tbl_actors.actor_lname
    FROM tbl_movies
    INNER JOIN tbl_actors ON actor_movie_id = movie_id;