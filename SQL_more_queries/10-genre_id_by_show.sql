-- Import the database dump from hbtn_0d_tvshows to your MySQL serve

SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows, tv_show_genres
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC