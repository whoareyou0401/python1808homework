/*
Navicat MySQL Data Transfer

Source Server         : 百度云
Source Server Version : 50723
Source Host           : 106.12.29.193:3306
Source Database       : zuqiudui

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-08-07 08:03:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for renyuan
-- ----------------------------
DROP TABLE IF EXISTS `renyuan`;
CREATE TABLE `renyuan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `age` varchar(16) DEFAULT NULL,
  `sex` varchar(4) DEFAULT NULL,
  `fire` varchar(20) DEFAULT NULL,
  `is_delete` int(11) DEFAULT '1',
  `zhiye` varchar(30) DEFAULT 'qiuyuan',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of renyuan
-- ----------------------------
INSERT INTO `renyuan` VALUES ('1', '胥重阳', '18', '男', '1200', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('2', '承恩哥', '18', '男', '1200', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('3', '军哥', '22', '男', '1800', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('4', '康哥', '19', '男', '1200', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('8', 'www', '19', '女', '1200', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('9', 'mengmeng', '22', '女', '1920', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('11', 'yun', '22', '女', '1800', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('12', 'feng', '22', '女', '1800', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('16', 'mengmeng', '22', '女', '1800', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('17', 'mengmeng', '22', '女', '1800', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('18', 'mengmeng', '22', '女', '1800', '1', 'qiuyuan');
INSERT INTO `renyuan` VALUES ('19', 'mengmeng', '22', '女', '1800', '1', 'qiuyuan');
