添加运动员表:
-- CREATE TABLE sport(id INT PRIMARY KEY auto_increment,NAME VARCHAR(20),age INT,sex INT,fire_out INT);
添加表数据内容：
-- INSERT INTO sport(NAME,age,sex,fire_out)VALUES("小虎",22,0,5000),("uzi",22,0,5000),("五五开",25,0,3000),("letme",24,0,4000),("UU",23,1,900);
添加一个字段：
-- ALTER TABLE sport ADD is_del INT DEFAULT 1;
设置一个约束 要求 name不能为空
-- ALTER TABLE sport MODIFY NAME VARCHAR(20) NOT NULL;
在表内添加数控：
-- INSERT INTO sport(NAME,age,sex,fire_out)VALUES("笑笑",30,0,999),("西卡",27,0,999),("阿怡",28,1,200);--
查看：
-- SELECT * FROM sport;
-- SELECT id,NAME,age,sex FROM sport;
-- SELECT NAME AS "姓名",age AS "年龄",sex AS "性别", fire_out AS "火力输出" FROM sport;
-- SELECT * FROM sport WHERE NAME LIKE "阿%" ;
-- select * from sport WHERE  age BETWEEN 20 and 30;
-- select * from sport limit 3;
-- select * from sport LIMIT 2 OFFSET 3;
-- select * from sport LIMIT 3,2;
-- select * from sport WHERE age  in (22,30);
