-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.

SELECT ts.`title`, tsg.`genre_id`
FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS tsg
ON ts.`id` = tsg.`show_id`
ORDER BY ts.`title`, tsg.`genre_id`;
 
