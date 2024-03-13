-- Lists all genres of the database hbtn_0d_tvshows
-- not linked to the show Dexter.
-- Records are sorted by ascending genre name.

SELECT DISTINCT `name`
FROM `tv_genres` AS tvg
INNER JOIN `tv_show_genres` AS tsg
ON tvg.`id` = tsg.`genre_id`
INNER JOIN `tv_shows` AS t
ON tsg.`show_id` = t.`id`
WHERE tvg.`name` NOT IN
(SELECT `name` 
FROM `tv_genres` AS tvg
INNER JOIN `tv_show_genres` AS tsg
ON tvg.`id` = tsg.`genre_id`
INNER JOIN `tv_shows` AS t
ON tsg.`show_id` = t.`id`
WHERE t.`title` = "Dexter")
ORDER BY tvg.`name`;
 
