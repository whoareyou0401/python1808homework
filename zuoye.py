how CREATE TABLE team
SELECT
CASE when fire_out > 1000 THEN "猛男"
else "菜鸡"
END
from team
team	CREATE TABLE `team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `fire_out` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8
SELECT
CASE WHEN sex = 0 THEN "男"
     WHEN sex = 1 THEN "女"
ELSE "保密"
END
