CREATE TABLE player(id int auto_increment PRIMARY KEY,name VARCHAR(30),age int,sex int,fire_out int);
-- INSERT into player(name,age,sex,fire_out) VALUES("姚明",36,0,1200);
-- INSERT into player(name,age,sex,fire_out) VALUES("叶莉",32,1,800),("朱婷",25,1,999),("乔丹",56,0,1099),("科比",42,0,880),("科比",42,0,1280),("科比1",42,2,880),("爱丽",26,1,980);

-- 查看表字段信息
-- desc player;

-- 删除 
-- INSERT into player(name,age,sex,fire_out) VALUES("丁宁",28,1,1001);
-- DELETE from player where name="丁宁";

-- 修改年龄字段属性不为空
-- ALTER table player modify age int NOT NULL;

-- 查询表的全部数据
-- SELECT *from player;

-- 查找名字像科比那样带有科(朱)字的所有人的信息
-- SELECT * from player where name like"科%" ;
-- SELECT * from player where name like"朱_" ;

-- 查找年龄在20和40之间的运动员的信息
-- select *from player where age BETWEEN 20 AND 40;

-- distin关键字
-- SELECT DISTINCT name from player;

-- in
-- SELECT * from player where fire_out in(800,880,980);

-- 查找活力值大于900的球员信息且只取两条
-- SELECT * from player where fire_out >900 LIMIT 2;

-- 给字段起别名
-- select name AS 姓名,age AS 年龄 from player;

-- 更新姚明为阿达
UPDATE player set name = "阿达" where name = "姚明";
