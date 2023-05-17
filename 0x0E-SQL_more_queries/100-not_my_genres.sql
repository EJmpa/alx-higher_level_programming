-- list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT gr.name FROM tv_genres AS gr
LEFT JOIN
(
       SELECT gr.id FROM tv_genres AS gr
       JOIN tv_show_genres AS shgr
       	    ON gr.id=shgr.genre_id
       JOIN tv_shows AS sh
       	    ON shgr.show_id=sh.id
       WHERE sh.title = "Dexter"
       ORDER BY gr.name ASC
) AS subdx
ON subdx.id = gr.id
WHERE subdx.id IS NULL
ORDER BY gr.name ASC;
