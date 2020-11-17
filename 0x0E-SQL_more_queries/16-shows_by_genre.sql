-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- do the thing
SELECT tv_shows.title, tv_genres.name
FROM tv_genres
Right JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
Right JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id
ORDER BY tv_shows.title, tv_genres.name ASC;