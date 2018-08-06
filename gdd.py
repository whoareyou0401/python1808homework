REATE TABLE staff(id INT auto_increment PRIMARY KEY,NAME VARCHAR(30),sex VARCHAR(4),POSITION VARCHAR(20));
-- DESC staff;
-- CREATE TABLE players(id INT auto_increment PRIMARY KEY,NAME VARCHAR(10),age INT,sex INT,fire_out INT);
-- 插入5条数据
-- INSERT INTO players(name,age,sex,fire_out) VALUES("科比","35","0","10000"),("麦迪","36","0","9000"),("科比","28","1","8000"),("易建联","40","0","7000"),("姚明","30","0","6000"),("傅园慧","24","1","5000");
-- 查询
-- SELECT * FROM players;

-- 查询名字是科比的信息
-- SELECT * FROM players WHERE name="科比";
-- SELECT id,NAME,age,sex FROM players;

-- 起别名
-- SELECT name as "姓名" FROM players;

-- 查询name 这一列1-4的信息
-- SELECT name FROM players WHERE id BETWEEN 1 and 4;

-- 查询ID 1-4的所有的信息
-- select * FROM players WHERE id BETWEEN 1 and 5;

-- 查询3条信息
-- SELECT * from players LIMIT 3;

-- 查询ID从2之后即3开始的三条信息
-- SELECT * FROM players LIMIT 3 OFFSET 2;

-- 从第二条之后即第三条开始取三条数据
-- SELECT * FROM players LIMIT 2,3;
 
-- 查询id为2,5,6的信息
-- select * FROM players WHERE id in (2,5,6);

-- 去重 DISTINCT
-- SELECT DISTINCT NAME FROM players;

-- 更新：将名为科比的改为丹丹
-- UPDATE players SET NAME="丹丹" WHERE name="科比"; 
-- UPDATE players set name="科比" WHERE NAME="丹丹";
