-- MySQL dump 10.13  Distrib 5.7.20, for osx10.11 (x86_64)
--
-- Host: localhost    Database: moive2
-- ------------------------------------------------------
-- Server version	5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `is_super` smallint(6) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `role_id` (`role_id`),
  KEY `ix_admin_addtime` (`addtime`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','pbkdf2:sha256:50000$HQDc89Lo$896c8f8f5b09d5d9ff0cc9a8c7c2308d9bc56c46c5736fb837cc9003398aeddf',0,1,'2018-05-05 23:20:32'),(2,'admin2','pbkdf2:sha256:50000$41yVEqFz$e79f73ccb7e92eb60796ac96d7c90ac822a7227506cd9d21d16e7a3c477d8f26',1,4,'2018-05-07 00:20:39'),(3,'admin3','pbkdf2:sha256:50000$kPZ0oAWg$3f169db698be05427eab3b9a6b04f33a9988b845252a63164c538c8d2e164f92',1,4,'2018-05-07 09:42:38');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adminlog`
--

DROP TABLE IF EXISTS `adminlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adminlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_adminlog_addtime` (`addtime`),
  CONSTRAINT `adminlog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adminlog`
--

LOCK TABLES `adminlog` WRITE;
/*!40000 ALTER TABLE `adminlog` DISABLE KEYS */;
INSERT INTO `adminlog` VALUES (1,1,'127.0.0.1','2018-05-06 10:23:20'),(2,1,'127.0.0.1','2018-05-06 10:24:13'),(3,1,'127.0.0.1','2018-05-06 11:09:30'),(4,1,'127.0.0.1','2018-05-06 11:18:59'),(5,1,'127.0.0.1','2018-05-06 17:15:55'),(6,1,'127.0.0.1','2018-05-06 17:22:09'),(7,1,'127.0.0.1','2018-05-06 17:23:15'),(8,1,'127.0.0.1','2018-05-06 17:27:08'),(9,1,'127.0.0.1','2018-05-06 17:35:44'),(10,1,'127.0.0.1','2018-05-06 17:37:56'),(11,1,'127.0.0.1','2018-05-06 17:38:37'),(12,1,'127.0.0.1','2018-05-06 17:40:25'),(13,1,'127.0.0.1','2018-05-06 17:46:44'),(14,1,'127.0.0.1','2018-05-06 20:06:27'),(15,2,'127.0.0.1','2018-05-07 00:21:00'),(16,2,'127.0.0.1','2018-05-07 20:44:11'),(17,1,'127.0.0.1','2018-05-07 20:53:32'),(18,2,'127.0.0.1','2018-05-07 20:56:36'),(19,1,'127.0.0.1','2018-05-09 23:15:59'),(20,2,'127.0.0.1','2018-05-09 23:16:22'),(21,1,'127.0.0.1','2018-05-09 23:36:47'),(22,3,'127.0.0.1','2018-05-12 09:45:28'),(23,3,'127.0.0.1','2018-05-14 00:32:19');
/*!40000 ALTER TABLE `adminlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth`
--

DROP TABLE IF EXISTS `auth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `url` (`url`),
  KEY `ix_auth_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth`
--

LOCK TABLES `auth` WRITE;
/*!40000 ALTER TABLE `auth` DISABLE KEYS */;
INSERT INTO `auth` VALUES (1,'权限列表','/admin/auth/<int:page>/','2018-05-06 19:40:07'),(3,'会员管理','/admin/userlist/<int:page>/','2018-05-06 19:43:49'),(4,'评论管理','/admin/commentlist/<int:page>/','2018-05-06 19:44:22'),(5,'浏览收藏列表','/admin/moviecollist/<int:page>/','2018-05-06 19:52:10'),(6,'添加预告','/admin/addpreview/','2018-05-06 19:52:39'),(7,'编辑预告','/admin/previeedit/','2018-05-06 19:53:15'),(8,'添加标签','/admin/addtag/','2018-05-06 19:54:23'),(9,'标签浏览','/admin/taglist/<int:page>/','2018-05-06 19:54:43'),(10,'编辑标签','/admin/tag/edit/','2018-05-06 19:55:03'),(11,'删除标签','/admin/tag/del/','2018-05-06 19:56:01'),(12,'管理员登录日志','/admin/adminlog/<int:page>/','2018-05-06 20:04:33'),(13,'浏览会员登录日志','/admin/userloginlog/<int:page>','2018-05-06 20:04:58'),(14,'添加电影','/admin/addmovie/','2018-05-09 23:37:02'),(15,'电影列表','/admin/movie/list/<int:page>/','2018-05-09 23:37:47');
/*!40000 ALTER TABLE `auth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `movie_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_id` (`movie_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_comment_addtime` (`addtime`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `moive` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (3,'非常受欢迎',3,44,'2018-05-06 06:59:39'),(4,'非常受欢迎',5,44,'2018-05-06 06:59:39'),(8,'非常受欢迎!',5,44,'2018-05-06 06:59:39'),(9,'非常受欢迎!',3,44,'2018-05-06 06:59:39'),(10,'非常受欢迎!',4,44,'2018-05-06 06:59:39'),(12,'雾都孤儿非常受欢迎!',6,4,'2018-05-06 06:59:39'),(13,'雾都孤儿非常受欢迎!',6,44,'2018-05-06 06:59:39'),(15,'雾都非常受欢迎!',7,4,'2018-05-06 06:59:39'),(16,'12345678',4,43,'2018-05-13 22:22:55'),(17,'12345678',4,43,'2018-05-13 22:22:59'),(18,'12345678910',4,4,'2018-05-13 22:23:25'),(19,'12345678910',4,44,'2018-05-13 22:27:01'),(20,'电影网站做的很不错，哈哈',4,44,'2018-05-13 22:27:29'),(21,'电影网站做的很不错，哈哈',4,44,'2018-05-13 22:27:34'),(22,'电影网站做的很不错，我很喜欢这个网站',4,43,'2018-05-13 22:27:44'),(23,'电影网站做的很不错，我很喜欢这个网站11',4,44,'2018-05-13 22:28:03'),(24,'信息技术科技公司',4,38,'2018-05-13 22:28:15'),(25,'大数据人工智能信息',4,38,'2018-05-13 22:28:25'),(26,'不需要相信别人  哈哈',4,43,'2018-05-13 22:28:44'),(27,'不需要相信别人  哈哈',4,43,'2018-05-13 22:35:58'),(28,'不需要相信别人  哈哈',4,43,'2018-05-13 22:36:05'),(29,'123444',4,43,'2018-05-13 22:37:04'),(30,'1234448888',4,43,'2018-05-13 22:37:10'),(31,'1234448888',4,43,'2018-05-13 22:38:32'),(32,'1234448888',4,43,'2018-05-13 22:39:47'),(33,'1233333333',4,43,'2018-05-13 22:39:55'),(34,'欢迎收看',4,43,'2018-05-13 22:40:13'),(35,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0024.gif\"/></p>',4,43,'2018-05-13 23:27:08'),(36,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0024.gif\"/></p>',4,43,'2018-05-13 23:27:50'),(37,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0002.gif\"/></p>',5,43,'2018-05-13 23:47:02'),(38,'<p>123</p>',5,43,'2018-05-13 23:49:06'),(39,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0014.gif\"/></p>',6,43,'2018-05-14 00:14:20'),(40,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0002.gif\"/></p>',6,43,'2018-05-14 00:14:32'),(41,'<p><a href=\"http://www.baidu.com\" target=\"_blank\" title=\"百度百度百度百度百度百度百度百度百度百度\">百度</a><img src=\"http://img.baidu.com/hi/jx2/j_0002.gif\"/></p>',6,43,'2018-05-14 00:15:56'),(42,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0014.gif\"/></p>',4,43,'2018-05-14 00:25:46'),(43,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0014.gif\"/></p>',4,43,'2018-05-14 09:38:48'),(44,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0001.gif\"/></p>',4,43,'2018-05-14 09:38:55'),(45,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0028.gif\"/></p>',4,43,'2018-05-19 18:52:40'),(46,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0016.gif\"/></p>',4,43,'2018-05-19 18:53:07'),(47,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0002.gif\"/></p>',5,43,'2018-05-19 20:43:45'),(48,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0017.gif\"/></p>',5,43,'2018-05-19 20:44:05'),(49,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0040.gif\"/></p>',5,43,'2018-05-19 20:44:37'),(50,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0046.gif\"/></p>',8,43,'2018-05-19 21:07:31'),(51,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0002.gif\"/></p>',7,43,'2018-05-19 23:11:27');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moive`
--

DROP TABLE IF EXISTS `moive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `moive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `info` text,
  `logo` varchar(255) DEFAULT NULL,
  `start` smallint(6) DEFAULT NULL,
  `playnum` bigint(20) DEFAULT NULL,
  `commentnum` bigint(20) DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `release_time` date DEFAULT NULL,
  `length` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `url` (`url`),
  UNIQUE KEY `logo` (`logo`),
  KEY `tag_id` (`tag_id`),
  KEY `ix_moive_addtime` (`addtime`),
  CONSTRAINT `moive_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moive`
--

LOCK TABLES `moive` WRITE;
/*!40000 ALTER TABLE `moive` DISABLE KEYS */;
INSERT INTO `moive` VALUES (3,'战狼','20180506014324c9623b1dd82944bfad5704b71a00f151.png','战狼','20180506014324223c78e42abe436c992ad7b5828967a6.png',5,9,9,4,'世界之巅','2018-05-18','15','2018-05-06 01:43:25'),(4,'唐朝历史','201805092344387b748fcc4cce443991ed226bc1d275c4.mp4','唐朝历史故事','201805060413232103e1d7704c4b2785cb0438b022c78a.jpeg',5,98,18,3,'马路','2018-05-20','20','2018-05-06 02:01:14'),(5,'MySQLDBA分析','20180506041734de74fd673d8f48ce9370a73c85600392.mp4','数据分析','2018050604173483308eee1f1b47b4b69d92e3cc8bdf25.jpg',3,38,27,4,'世界之巅','2018-05-25','120','2018-05-06 04:17:34'),(6,'雾都孤儿','20180509234359e65c6f61eaf64315b3766a39d009abca.mp4','雾都孤儿\r\n雾都孤儿\r\n雾都孤儿\r\n雾都孤儿','20180506062500ebb7c58f3e774922a753635efe422324.jpeg',1,10,7,2,'南极','2018-05-31','120','2018-05-06 06:25:01'),(7,'雾都','201805092343143c83c60f8c23432a9420c9148608052a.mp4','雾都\r\n','20180506062544b883a36278634baf95a742eb8d8d57e2.jpeg',1,5,4,8,'香港','2018-05-17','15','2018-05-06 06:25:44'),(8,'新发展 新方向2','201805092342332548147c4e06494eb7a026572bedc7fe.mp4','新发展 新方向','20180506103545e61977e1b51d47679cd290ff94d06b29.jpeg',3,4,3,8,'南极','2018-05-20','10','2018-05-06 10:35:46'),(9,'西数国际','201805092341288678de9dd5874499bf69c144ad463f9a.mp4','西数国际','20180509234128a120ac85353e40edbf29497300e44c86.png',5,0,0,7,'北京','2018-05-11','14','2018-05-09 23:41:28');
/*!40000 ALTER TABLE `moive` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moviecol`
--

DROP TABLE IF EXISTS `moviecol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `moviecol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_id` (`movie_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_moviecol_addtime` (`addtime`),
  CONSTRAINT `moviecol_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `moive` (`id`),
  CONSTRAINT `moviecol_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moviecol`
--

LOCK TABLES `moviecol` WRITE;
/*!40000 ALTER TABLE `moviecol` DISABLE KEYS */;
INSERT INTO `moviecol` VALUES (1,4,4,'2018-05-06 09:05:00'),(4,4,17,'2018-05-06 09:10:05'),(5,4,14,'2018-05-06 09:10:05'),(6,4,18,'2018-05-06 09:10:05'),(7,3,14,'2018-05-06 09:10:05'),(9,4,18,'2018-05-06 09:10:05'),(15,5,4,'2018-05-06 09:11:17'),(18,5,18,'2018-05-06 09:11:20'),(20,3,4,'2018-05-06 09:11:20'),(22,5,17,'2018-05-06 09:11:24'),(23,5,14,'2018-05-06 09:11:24'),(26,3,4,'2018-05-06 09:11:24'),(27,5,43,'2018-05-19 21:04:07'),(28,3,43,'2018-05-19 21:05:05'),(29,6,43,'2018-05-19 21:06:35'),(30,8,43,'2018-05-19 21:07:36');
/*!40000 ALTER TABLE `moviecol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oplog`
--

DROP TABLE IF EXISTS `oplog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oplog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `reason` varchar(600) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_oplog_addtime` (`addtime`),
  CONSTRAINT `oplog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oplog`
--

LOCK TABLES `oplog` WRITE;
/*!40000 ALTER TABLE `oplog` DISABLE KEYS */;
INSERT INTO `oplog` VALUES (1,1,'127.0.0.1','添加标签tdops','2018-05-06 10:28:14'),(2,1,'127.0.0.1','添加标签tdops1','2018-05-06 10:28:17'),(3,1,'127.0.0.1','添加标签tdops2','2018-05-06 10:28:20'),(4,1,'127.0.0.1','添加标签123','2018-05-06 10:28:24'),(5,1,'127.0.0.1','添加标签124','2018-05-06 10:28:27'),(6,1,'127.0.0.1','添加标签125','2018-05-06 10:28:31'),(7,1,'127.0.0.1','删除标签成功<Tag \'123\'>','2018-05-06 10:30:17'),(8,1,'127.0.0.1','删除标签成功<Tag \'124\'>','2018-05-06 10:30:19'),(9,1,'127.0.0.1','删除标签成功125','2018-05-06 10:30:42'),(10,1,'127.0.0.1','删除标签成功tdops2','2018-05-06 10:30:44'),(11,1,'127.0.0.1','删除标签成功tdops1','2018-05-06 10:30:45'),(12,1,'127.0.0.1','编辑标签成功!自动化运维','2018-05-06 10:33:00'),(13,1,'127.0.0.1','添加电影成功新发展 新方向','2018-05-06 10:35:46'),(14,1,'127.0.0.1','编辑电影成功新发展 新方向2','2018-05-06 10:37:37'),(15,1,'127.0.0.1','添加预告成功新发展方向','2018-05-06 10:39:38'),(16,1,'127.0.0.1','编辑预告成功新发展方向jenkins -CI CD','2018-05-06 10:41:30'),(17,1,'127.0.0.1','删除收藏成功5','2018-05-06 10:46:03'),(18,1,'127.0.0.1','删除收藏成功ID编号为5，收藏用户为4','2018-05-06 10:47:24'),(19,1,'127.0.0.1','删除收藏成功ID编号为5，收藏用户为4','2018-05-06 10:47:57'),(20,1,'127.0.0.1','删除收藏成功ID编号为5，收藏用户为18','2018-05-06 10:47:58'),(21,1,'127.0.0.1','删除收藏成功ID编号为5，收藏用户为14','2018-05-06 10:48:00'),(22,1,'127.0.0.1','删除评论ID编号为6，收藏用户为该教材非常受欢迎!','2018-05-06 10:50:28'),(23,1,'127.0.0.1','删除收藏成功ID编号为5，收藏用户为17','2018-05-06 11:19:30'),(24,1,'127.0.0.1','删除收藏成功ID编号为3，收藏用户为4','2018-05-06 11:19:33'),(25,1,'127.0.0.1','删除收藏成功ID编号为5，收藏用户为17','2018-05-06 11:19:49'),(26,1,'127.0.0.1','admin用户修改密码成功！','2018-05-06 17:46:36'),(27,1,'127.0.0.1','添加权限配置权限成功！','2018-05-06 19:40:07'),(28,1,'127.0.0.1','添加操作日志权限成功！','2018-05-06 19:41:55'),(29,1,'127.0.0.1','添加会员管理权限成功！','2018-05-06 19:43:49'),(30,1,'127.0.0.1','添加评论管理权限成功！','2018-05-06 19:44:22'),(31,1,'127.0.0.1','添加收藏列表浏览权限权限成功！','2018-05-06 19:52:10'),(32,1,'127.0.0.1','添加添加预告权限成功！','2018-05-06 19:52:39'),(33,1,'127.0.0.1','添加编辑预告权限成功！','2018-05-06 19:53:15'),(34,1,'127.0.0.1','添加添加标签权限成功！','2018-05-06 19:54:23'),(35,1,'127.0.0.1','添加标签浏览权限成功！','2018-05-06 19:54:43'),(36,1,'127.0.0.1','添加编辑标签权限成功！','2018-05-06 19:55:03'),(37,1,'127.0.0.1','添加删除标签权限成功！','2018-05-06 19:56:01'),(38,1,'127.0.0.1','删除权限成功，权限名称为：操作日志，地址为:/admin/oplog/','2018-05-06 20:02:39'),(39,1,'127.0.0.1','添加管理员登录日志权限成功！','2018-05-06 20:04:33'),(40,1,'127.0.0.1','添加会员登录日志权限成功！','2018-05-06 20:04:58'),(41,1,'127.0.0.1','编辑权限成功浏览会员登录日志，地址为：/admin/userloginlog/','2018-05-06 20:34:30'),(42,1,'127.0.0.1','编辑权限成功浏览收藏列表，地址为：/admin/moviecollist/','2018-05-06 20:34:52'),(43,1,'127.0.0.1','添加软件开发角色成功！','2018-05-06 21:41:02'),(44,1,'127.0.0.1','添加管理员属性角色成功！','2018-05-06 21:41:56'),(45,1,'127.0.0.1','编辑管理员属性1角色成功，','2018-05-06 23:19:32'),(46,1,'127.0.0.1','成功删除软件开发角色！','2018-05-06 23:29:31'),(47,1,'127.0.0.1','成功删除管理员属性1角色！','2018-05-06 23:29:39'),(48,1,'127.0.0.1','添加系统管理员角色成功！','2018-05-06 23:30:04'),(49,1,'127.0.0.1','添加日志管理员角色成功！','2018-05-06 23:30:28'),(50,1,'127.0.0.1','添加admin2管理员成功！','2018-05-07 00:20:39'),(51,2,'127.0.0.1','添加admin3管理员成功！','2018-05-07 09:42:38'),(52,1,'127.0.0.1','编辑权限成功浏览会员登录日志，地址为：/admin/userloginlog/<int:page>','2018-05-07 20:55:08'),(53,1,'127.0.0.1','编辑权限成功评论管理，地址为：/admin/commentlist/<int:page>/','2018-05-07 20:55:36'),(54,1,'127.0.0.1','编辑权限成功标签浏览，地址为：/admin/taglist/<int:page>/','2018-05-07 20:55:56'),(55,2,'127.0.0.1','编辑权限成功管理员登录日志，地址为：/admin/adminlog/<int:page>/','2018-05-07 20:58:55'),(56,2,'127.0.0.1','编辑权限成功浏览收藏列表，地址为：/admin/moviecollist/<int:page>/','2018-05-07 20:59:15'),(57,2,'127.0.0.1','编辑权限成功会员管理，地址为：/admin/userlist/<int:page>/','2018-05-07 21:17:51'),(58,2,'127.0.0.1','编辑权限成功权限列表，地址为：/admin/auth/<int:page>/','2018-05-07 21:18:38'),(59,2,'127.0.0.1','添加预告成功花果树','2018-05-09 23:18:52'),(60,2,'127.0.0.1','添加预告成功无心果实','2018-05-09 23:19:10'),(61,2,'127.0.0.1','添加预告成功美丽的花朵','2018-05-09 23:19:28'),(62,2,'127.0.0.1','添加预告成功天使的眼泪','2018-05-09 23:19:49'),(63,1,'127.0.0.1','添加添加电影权限成功！','2018-05-09 23:37:02'),(64,1,'127.0.0.1','添加电影列表权限成功！','2018-05-09 23:37:47'),(65,1,'127.0.0.1','编辑日志管理员角色成功，','2018-05-09 23:38:29'),(66,1,'127.0.0.1','编辑普通管理员角色成功，','2018-05-09 23:38:53'),(67,1,'127.0.0.1','添加电影成功西数国际','2018-05-09 23:41:28'),(68,1,'127.0.0.1','编辑电影成功新发展 新方向2','2018-05-09 23:42:33'),(69,1,'127.0.0.1','编辑电影成功雾都','2018-05-09 23:43:14'),(70,1,'127.0.0.1','编辑电影成功雾都孤儿','2018-05-09 23:44:00'),(71,1,'127.0.0.1','编辑电影成功唐朝历史','2018-05-09 23:44:39');
/*!40000 ALTER TABLE `oplog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perview`
--

DROP TABLE IF EXISTS `perview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `perview` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `logo` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `logo` (`logo`),
  KEY `ix_perview_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perview`
--

LOCK TABLES `perview` WRITE;
/*!40000 ALTER TABLE `perview` DISABLE KEYS */;
INSERT INTO `perview` VALUES (2,'战狼之光','20180506045236b436d497c49a4a48801f1cde50a43900.jpg','2018-05-06 04:52:37'),(3,'中国之光','20180506050441f7981b14c07344e4abc92bb1512a2781.jpg','2018-05-06 05:04:42'),(4,'记得你的好','20180506050512fcfd3ebce4df4991972dcd25fb131006.png','2018-05-06 05:05:13'),(5,'云计算支撑','201805060505240a6268133aef438f89bac65831ed3c30.jpg','2018-05-06 05:05:24'),(6,'精武门','20180506054420a83ca34e74ac4fada3ab9612ee39dd62.jpg','2018-05-06 05:44:20'),(7,'雾都孤儿','201805060545062a89f297d9114169bd9336293ceff25f.jpg','2018-05-06 05:45:06'),(8,'新发展方向jenkins -CI CD','2018050610393788cebf0600e94f4db32030030ec8bbb6.jpeg','2018-05-06 10:39:38'),(9,'花果树','20180509231852adf032a955fc4cff85716562c85598bd.jpeg','2018-05-09 23:18:52'),(10,'无心果实','20180509231909630bbe7a5861411aa9c1532832c75f26.png','2018-05-09 23:19:10'),(11,'美丽的花朵','201805092319281908463e383e46f9a19946701a811f28.jpg','2018-05-09 23:19:28'),(12,'天使的眼泪','20180509231949b549f2e0466b41e1b5208e94454e916e.jpg','2018-05-09 23:19:49');
/*!40000 ALTER TABLE `perview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `auths` varchar(600) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `auths` (`auths`),
  KEY `ix_role_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'普通管理员','1,3,5,7,9,10,11,12,13','2018-05-05 23:20:16'),(4,'系统管理员','1,3,4,5,6,7,8,9,10,11,12,13','2018-05-06 23:30:04'),(5,'日志管理员','6,7,8,12,13','2018-05-06 23:30:28');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_tag_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (2,'软件开发','2018-05-05 23:21:48'),(3,'历史数据','2018-05-05 23:24:54'),(4,'未来之星','2018-05-05 23:25:08'),(5,'文学类','2018-05-06 04:15:24'),(6,'爱情','2018-05-06 05:40:17'),(7,'都市类','2018-05-06 05:40:24'),(8,'言情类','2018-05-06 05:40:34'),(9,'军事','2018-05-06 05:40:44'),(10,'互联网金融行业','2018-05-06 05:41:04'),(11,'大数据','2018-05-06 05:41:18'),(12,'通信行业','2018-05-06 05:41:29'),(13,'历史数据之谜','2018-05-06 05:41:39'),(14,'自动化运维','2018-05-06 10:28:14');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `info` text,
  `face` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `face` (`face`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `ix_user_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (4,'李四','12345678','1343@163.com','18393302719','资深架构师总共','bg1.jpg','2018-05-06 08:26:23','3c410569ac9d428f999e3a0730cb4201'),(14,'小精灵','12345900','1335333@162.com','18393302700','架构师','ad.jpg','2018-05-06 08:34:18','3c410569ac9d428f999e3a0730cb4ss222'),(17,'精灵','123s45900','1335333@16s2.com','13393302700','架构师','ad2.jpg','2018-05-06 08:35:56','3c4s10569ac9d428f999e3a0730cb4ss222'),(18,'李开','1237s82','13453@16s1.com','13893302712','总经理助理','bg3.jpg','2018-05-06 08:35:56','3c4s10569ac9d428f999e3a0730cb420ssfff22'),(38,'123','pbkdf2:sha256:50000$3oPloVn8$5a684f5877d1be3126b4cfc5a69a94b8c675c01938a4bc093f29e4f42f459900','admin2@admin.com','18393358061',NULL,'ad4.jpg','2018-05-08 00:08:00','892b0fa0b0804178b0847ba9c14abe8b'),(43,'admin3','pbkdf2:sha256:50000$3F7By7wm$9a1281050bef357fa166717006fab6f106be95db4cb645c00534ba3a24005836','admin123@163.com','18393358069','江山代有人才出，各领风骚数百年!','201805090100014c2cf14a75ca484aa2cb3e72bd87c4ea.png','2018-05-08 00:41:31','6500241b09a84f2e85691639357e2a22'),(44,'admin4','pbkdf2:sha256:50000$REURgfnz$776f7a82ecf33ffc514cffcba343216515ab5afcbc56edd491dde9d38b40a773','admin4@admin4.com','18393358080','留取丹心照汗青','2018050907554903c43135e0c64d5b959c89d8baa7d8bb.jpg','2018-05-09 07:55:03','6c766ad82de448e6a2646c0878424ced');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userlog`
--

DROP TABLE IF EXISTS `userlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `ix_userlog_addtime` (`addtime`),
  CONSTRAINT `userlog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=173 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlog`
--

LOCK TABLES `userlog` WRITE;
/*!40000 ALTER TABLE `userlog` DISABLE KEYS */;
INSERT INTO `userlog` VALUES (81,4,'127.0.0.1','2018-05-06 11:44:13'),(82,14,'127.0.0.1','2018-05-06 11:44:13'),(83,17,'127.0.0.1','2018-05-06 11:44:13'),(84,18,'127.0.0.1','2018-05-06 11:44:13'),(85,4,'127.0.0.1','2018-05-06 11:44:14'),(86,14,'127.0.0.1','2018-05-06 11:44:14'),(87,17,'127.0.0.1','2018-05-06 11:44:14'),(88,18,'127.0.0.1','2018-05-06 11:44:14'),(89,4,'127.0.0.1','2018-05-06 11:44:15'),(90,14,'127.0.0.1','2018-05-06 11:44:15'),(91,17,'127.0.0.1','2018-05-06 11:44:15'),(92,18,'127.0.0.1','2018-05-06 11:44:15'),(93,4,'127.0.0.1','2018-05-06 11:44:16'),(94,14,'127.0.0.1','2018-05-06 11:44:16'),(95,17,'127.0.0.1','2018-05-06 11:44:16'),(96,18,'127.0.0.1','2018-05-06 11:44:16'),(97,4,'127.0.0.1','2018-05-06 11:44:17'),(98,14,'127.0.0.1','2018-05-06 11:44:17'),(99,17,'127.0.0.1','2018-05-06 11:44:17'),(100,18,'127.0.0.1','2018-05-06 11:44:17'),(101,4,'127.0.0.1','2018-05-06 11:44:18'),(102,14,'127.0.0.1','2018-05-06 11:44:18'),(103,17,'127.0.0.1','2018-05-06 11:44:18'),(104,18,'127.0.0.1','2018-05-06 11:44:18'),(105,4,'127.0.0.1','2018-05-06 11:44:42'),(106,14,'127.0.0.1','2018-05-06 11:44:42'),(107,17,'127.0.0.1','2018-05-06 11:44:42'),(108,18,'127.0.0.1','2018-05-06 11:44:42'),(109,4,'127.0.0.1','2018-05-06 11:44:43'),(110,14,'127.0.0.1','2018-05-06 11:44:43'),(111,17,'127.0.0.1','2018-05-06 11:44:43'),(112,18,'127.0.0.1','2018-05-06 11:44:43'),(113,4,'127.0.0.1','2018-05-06 11:44:43'),(114,14,'127.0.0.1','2018-05-06 11:44:43'),(115,17,'127.0.0.1','2018-05-06 11:44:43'),(116,18,'127.0.0.1','2018-05-06 11:44:43'),(117,4,'127.0.0.1','2018-05-06 11:44:44'),(118,14,'127.0.0.1','2018-05-06 11:44:44'),(119,17,'127.0.0.1','2018-05-06 11:44:44'),(120,18,'127.0.0.1','2018-05-06 11:44:44'),(121,4,'127.0.0.1','2018-05-06 11:44:44'),(122,14,'127.0.0.1','2018-05-06 11:44:44'),(123,17,'127.0.0.1','2018-05-06 11:44:44'),(124,18,'127.0.0.1','2018-05-06 11:44:44'),(125,4,'127.0.0.1','2018-05-06 11:44:45'),(126,14,'127.0.0.1','2018-05-06 11:44:45'),(127,17,'127.0.0.1','2018-05-06 11:44:45'),(128,18,'127.0.0.1','2018-05-06 11:44:45'),(129,43,'127.0.0.1','2018-05-08 00:50:33'),(130,43,'127.0.0.1','2018-05-08 00:52:20'),(131,43,'127.0.0.1','2018-05-08 00:52:58'),(132,43,'127.0.0.1','2018-05-08 00:53:29'),(133,43,'127.0.0.1','2018-05-08 01:07:06'),(134,43,'127.0.0.1','2018-05-09 01:18:26'),(135,43,'127.0.0.1','2018-05-09 01:18:45'),(136,43,'127.0.0.1','2018-05-09 07:49:22'),(137,43,'127.0.0.1','2018-05-09 07:50:42'),(138,43,'10.21.46.17','2018-05-09 07:52:35'),(139,43,'10.21.46.18','2018-05-09 07:52:40'),(140,43,'10.21.46.10','2018-05-09 07:52:47'),(141,43,'10.21.46.11','2018-05-09 07:53:21'),(142,43,'10.21.46.11','2018-05-09 07:53:21'),(143,43,'10.21.46.11','2018-05-09 07:53:21'),(144,43,'10.21.46.11','2018-05-09 07:53:23'),(145,43,'10.21.46.11','2018-05-09 07:53:23'),(146,43,'10.21.46.11','2018-05-09 07:53:23'),(147,43,'10.21.46.11','2018-05-09 07:53:24'),(148,43,'10.21.46.11','2018-05-09 07:53:24'),(149,43,'10.21.46.11','2018-05-09 07:53:24'),(150,43,'10.21.46.11','2018-05-09 07:53:25'),(151,43,'10.21.46.11','2018-05-09 07:53:25'),(152,43,'10.21.46.11','2018-05-09 07:53:25'),(153,43,'10.21.46.11','2018-05-09 07:53:26'),(154,43,'10.21.46.11','2018-05-09 07:53:26'),(155,43,'10.21.46.11','2018-05-09 07:53:26'),(156,43,'10.21.46.11','2018-05-09 07:53:26'),(157,43,'10.21.46.11','2018-05-09 07:53:26'),(158,43,'10.21.46.11','2018-05-09 07:53:26'),(159,43,'10.21.46.11','2018-05-09 07:53:27'),(160,43,'10.21.46.11','2018-05-09 07:53:27'),(161,43,'10.21.46.11','2018-05-09 07:53:27'),(162,43,'127.0.0.1','2018-05-09 07:53:40'),(163,44,'127.0.0.1','2018-05-09 07:55:16'),(164,43,'127.0.0.1','2018-05-09 08:05:33'),(165,43,'127.0.0.1','2018-05-09 08:15:22'),(166,43,'127.0.0.1','2018-05-09 22:56:01'),(167,44,'127.0.0.1','2018-05-13 20:37:51'),(168,43,'127.0.0.1','2018-05-13 22:13:27'),(169,44,'127.0.0.1','2018-05-14 00:10:35'),(170,43,'127.0.0.1','2018-05-14 00:12:19'),(171,43,'127.0.0.1','2018-05-14 00:12:41'),(172,43,'127.0.0.1','2018-05-19 18:52:23');
/*!40000 ALTER TABLE `userlog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-20  0:34:26
