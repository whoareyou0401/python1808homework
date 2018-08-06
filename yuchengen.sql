
CREATE TABLE qiuyuanbiao(
id INT auto_increment PRIMARY KEY,
q_name VARCHAR(40),
age INT,
sex INT CHECK(sex=1 OR sex=0 OR sex=2),
fire_out INT
) CHARSET="utf8";


INSERT INTO qiuyuanbiao VALUES(1,"于承恩",22,1,2000);
INSERT INTO qiuyuanbiao VALUES(2,"薛康康",22,1,1200);
INSERT INTO qiuyuanbiao VALUES(3,"胥重阳",21,1,1600);
INSERT INTO qiuyuanbiao VALUES(4,"张帅军",20,1,800);
INSERT INTO qiuyuanbiao VALUES(5,"杨洋",19,1,900);
INSERT INTO qiuyuanbiao VALUES(6,"包韵格",18,0,200);

SHOW CREATE TABLE qiuyuanbiao

UPDATE qiuyuanbiao SET age=24 WHERE q_name="薛康康";
UPDATE qiuyuanbiao SET age=24 WHERE q_name="于承恩";
DELETE from qiuyuanbiao where id = 4;
SELECT q_name,(CASE WHEN sex=1 then "男" ELSE case when sex = 0 then "女" else "保密" END END),(CASE WHEN fire_out >=1000 then "火力猛男" else "菜鸡" END) from qiuyuanbiao;
