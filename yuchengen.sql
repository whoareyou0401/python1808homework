
CREATE TABLE qiuyuanbiao(
id INT auto_increment PRIMARY KEY,
q_name VARCHAR(40),
age INT,
sex INT CHECK(sex=1 OR sex=0 OR sex=2),
fire_out INT
) CHARSET="utf8";


INSERT INTO qiuyuanbiao VALUES(1,"�ڳж�",22,1,2000);
INSERT INTO qiuyuanbiao VALUES(2,"Ѧ����",22,1,1200);
INSERT INTO qiuyuanbiao VALUES(3,"������",21,1,1600);
INSERT INTO qiuyuanbiao VALUES(4,"��˧��",20,1,800);
INSERT INTO qiuyuanbiao VALUES(5,"����",19,1,900);
INSERT INTO qiuyuanbiao VALUES(6,"���ϸ�",18,0,200);

SHOW CREATE TABLE qiuyuanbiao

UPDATE qiuyuanbiao SET age=24 WHERE q_name="Ѧ����";
UPDATE qiuyuanbiao SET age=24 WHERE q_name="�ڳж�";
DELETE from qiuyuanbiao where id = 4;
SELECT q_name,(CASE WHEN sex=1 then "��" ELSE case when sex = 0 then "Ů" else "����" END END),(CASE WHEN fire_out >=1000 then "��������" else "�˼�" END) from qiuyuanbiao;
