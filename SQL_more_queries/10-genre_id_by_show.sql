-- Import the database dump from hbtn_0d_tvshows to your MySQL serve

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows JOIN tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
