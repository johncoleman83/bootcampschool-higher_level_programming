-- lists all genres from btcp_0d_tvshows and displays the number of
-- shows linked to each
SELECT tv_genres.name AS genre,
	   COUNT(tv_show_genres.genre_id) AS number_shows
       FROM tv_genres INNER JOIN tv_show_genres
       ON tv_show_genres.genre_id = tv_genres.id
       GROUP BY tv_genres.name
       ORDER BY number_shows DESC;
