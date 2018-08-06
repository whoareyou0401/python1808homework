-- CREATE TABLE player(id INT(10)PRIMARY KEY auto_increment ,name VARCHAR(20),age INT(10),sex INT(6),fire_out INT(20));
-- desc player;
-- INSERT INTO player(name,age,sex,fire_out) VALUES("阿达","18","1","100");
-- INSERT INTO player(name,age,sex,fire_out) VALUES("jeams","32","1","1000"),("kabby","38","1","999");
-- INSERT INTO player VALUES("5","柳岩","38","0","1000");
-- desc player;
-- INSERT INTO player VALUES("6","潘晓婷","38","0","1000"),("7","易建联","32","1","10");
-- SELECT * FROM player;
-- SELECT name ,age, sex FROM player;
-- SELECT name as 姓名,age as 年龄,sex as 性别 from player;
-- SELECT * FROM player where name = "柳岩"; 
-- SELECT * from player  WHERE id BETWEEN   1 and 3;
-- cdSELECT * from player WHERE name LIKE "柳%";
-- SELECT * from player where  id >0 LIMIT 3 OFFSET 2;
-- SELECT * FROM player WHERE id in (1,3,4);
-- SELECT * FROM player WHERE id>3 and name="柳岩";
-- SELECT DISTINCT name from player;
-- DELETE from player WHERE name ="kabby";



