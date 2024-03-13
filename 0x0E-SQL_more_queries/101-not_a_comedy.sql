-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.

SELECT DISTINCT `title`
FROM `tv_shows` AS ts
LEFT JOIN `tv_show_genres` AS tsg
ON tsg.`show_id` = ts.`id`
LEFT JOIN `tv_genres` AS tg
ON tg.`id` = tsg.`genre_id`
WHERE ts.`title` NOT IN
(SELECT `title`
FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS tsg
ON tsg.`show_id` = ts.`id`
INNER JOIN `tv_genres` AS tg
ON tg.`id` = tsg.`genre_id`
WHERE tg.`name` = "Comedy"
)
ORDER BY ts.`title`;
 
