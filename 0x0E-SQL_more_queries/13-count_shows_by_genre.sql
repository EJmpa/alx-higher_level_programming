-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.
SELECT genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM genres
INNER JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id
HAVING COUNT(tv_show_genres.tv_show_id) > 0
ORDER BY number_of_shows DESC;
