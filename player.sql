/*
Navicat MySQL Data Transfer

Source Server         : 虚拟机mysql
Source Server Version : 50723
Source Host           : 192.168.133.137:3306
Source Database       : py1808

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-08-06 21:18:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for player
-- ----------------------------
DROP TABLE IF EXISTS `player`;
CREATE TABLE `player` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `age` int(100) DEFAULT NULL,
  `sex` int(5) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `fire_out` int(11) DEFAULT '1',
  `is_delete` int(11) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of player
-- ----------------------------
INSERT INTO `player` VALUES ('1', '小明', '20', '1', '大前锋', '1231', '1');
INSERT INTO `player` VALUES ('2', '小红', '18', '0', '中锋', '999', '1');
INSERT INTO `player` VALUES ('3', '李四', '24', '1', '后卫', '1738', '1');
INSERT INTO `player` VALUES ('4', '张三', '19', '1', '小前锋', '234', '1');
INSERT INTO `player` VALUES ('5', '小依', '25', '0', '中锋', '97846', '1');
INSERT INTO `player` VALUES ('6', '赵六', '30', '1', '裁判', '888', '1');
