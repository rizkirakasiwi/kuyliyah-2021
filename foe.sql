-- MariaDB dump 10.19  Distrib 10.4.18-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: foe
-- ------------------------------------------------------
-- Server version	10.4.18-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `school_code` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,'M Azizudin','YSPM','mazizudin@gmail.com','123qweawd');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homeroom_teacher`
--

DROP TABLE IF EXISTS `homeroom_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `homeroom_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_email` varchar(50) NOT NULL,
  `class_id` int(11) NOT NULL,
  `school_code` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_email` (`teacher_email`),
  KEY `class_id` (`class_id`),
  KEY `school_code` (`school_code`),
  CONSTRAINT `homeroom_teacher_ibfk_1` FOREIGN KEY (`teacher_email`) REFERENCES `teacher` (`email`),
  CONSTRAINT `homeroom_teacher_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `student_class` (`id`),
  CONSTRAINT `homeroom_teacher_ibfk_3` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homeroom_teacher`
--

LOCK TABLES `homeroom_teacher` WRITE;
/*!40000 ALTER TABLE `homeroom_teacher` DISABLE KEYS */;
/*!40000 ALTER TABLE `homeroom_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(20) NOT NULL,
  `time` varchar(10) NOT NULL,
  `school_code` varchar(20) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES (25,'17184065','02:12:20','YSPM','2021-09-01');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schools`
--

DROP TABLE IF EXISTS `schools`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schools` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` char(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schools`
--

LOCK TABLES `schools` WRITE;
/*!40000 ALTER TABLE `schools` DISABLE KEYS */;
INSERT INTO `schools` VALUES (1,'YSPM','SMK YASPIM');
/*!40000 ALTER TABLE `schools` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `uid` char(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone_number` char(12) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_code` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `class_id` (`class_id`),
  KEY `school_code` (`school_code`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `student_class` (`id`),
  CONSTRAINT `student_ibfk_2` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('17184065','Rizki Rakasiwi','085794626977',1,'rizkirakasiwirizki@gmail.com','d1f5b2627f67d6ed146a6b775ebf6029eb97ff298ce64f6acd13e4d78cd4fa8e821d13ad544d9f3bdf5ea2519c4acea4280a031ba9c50f6b0108d1df7a83d47c46e9503dd1e57496db29e6b218f5b496825cb2d221813a34f6',6,'YSPM'),('17184066','Samsul Arifin','085794637876',1,'samsul_arifin@gmail.com','d4a018d5d50ce6d2e0b950aaf3bef0a507e698acf9cdf1f87dedb253bfd619eb4a1b693d3663ef80bcbf8c09b79b187dfdd48e08ce68613fdbe63b0b1f8eaccd5b55529068cea087aa3386c2fe7459e7825f6de9391eac8f96',7,'YSPM');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_attendance`
--

DROP TABLE IF EXISTS `student_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_attendance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time_out` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `school_code` char(20) NOT NULL,
  `time_in` varchar(10) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `email` (`email`),
  KEY `school_code` (`school_code`),
  CONSTRAINT `student_attendance_ibfk_1` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`),
  CONSTRAINT `student_attendance_ibfk_2` FOREIGN KEY (`email`) REFERENCES `student` (`email`),
  CONSTRAINT `student_attendance_ibfk_3` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_attendance`
--

LOCK TABLES `student_attendance` WRITE;
/*!40000 ALTER TABLE `student_attendance` DISABLE KEYS */;
INSERT INTO `student_attendance` VALUES (87,'2021-09-01',NULL,'rizkirakasiwirizki@gmail.com','YSPM','02:12:20',NULL);
/*!40000 ALTER TABLE `student_attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_attendance_time`
--

DROP TABLE IF EXISTS `student_attendance_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_attendance_time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_in` time DEFAULT NULL,
  `time_out` time DEFAULT NULL,
  `school_code` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `school_code` (`school_code`),
  CONSTRAINT `student_attendance_time_ibfk_1` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_attendance_time`
--

LOCK TABLES `student_attendance_time` WRITE;
/*!40000 ALTER TABLE `student_attendance_time` DISABLE KEYS */;
INSERT INTO `student_attendance_time` VALUES (1,'07:00:00','13:00:00','YSPM');
/*!40000 ALTER TABLE `student_attendance_time` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_class`
--

DROP TABLE IF EXISTS `student_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `school_code` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `school_code` (`school_code`),
  CONSTRAINT `student_class_ibfk_1` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_class`
--

LOCK TABLES `student_class` WRITE;
/*!40000 ALTER TABLE `student_class` DISABLE KEYS */;
INSERT INTO `student_class` VALUES (1,'12 RPL 1','');
/*!40000 ALTER TABLE `student_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher` (
  `uid` char(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone_number` char(12) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_code` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `school_code` (`school_code`),
  CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`),
  CONSTRAINT `teacher_ibfk_2` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES ('13144001','Muhammad Labib','085794626977','mlabib@gmail.com','f6281d46f43b84c3568bbcf041999bd29c56c49c884535cd73ee8f3a419ff9c38b85f6219ee5b434104ed367a5e371c8fead0811d5dc69d25057c5b53e901027e42c5947fd35305081bdadf140f5055bd7d4065055a2dafc68',1,'YSPM');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_attendance`
--

DROP TABLE IF EXISTS `teacher_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_attendance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time_out` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `school_code` char(20) NOT NULL,
  `status_in` tinyint(1) DEFAULT NULL,
  `status_out` tinyint(1) DEFAULT NULL,
  `time_in` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `email` (`email`),
  KEY `school_code` (`school_code`),
  CONSTRAINT `teacher_attendance_ibfk_1` FOREIGN KEY (`email`) REFERENCES `teacher` (`email`),
  CONSTRAINT `teacher_attendance_ibfk_2` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_attendance`
--

LOCK TABLES `teacher_attendance` WRITE;
/*!40000 ALTER TABLE `teacher_attendance` DISABLE KEYS */;
INSERT INTO `teacher_attendance` VALUES (3,'2021-08-29','20:35:10','mlabib@gmail.com','YSPM',NULL,NULL,NULL);
/*!40000 ALTER TABLE `teacher_attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_attendance_time`
--

DROP TABLE IF EXISTS `teacher_attendance_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_attendance_time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_in` time DEFAULT NULL,
  `time_out` time DEFAULT NULL,
  `school_code` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `school_code` (`school_code`),
  CONSTRAINT `teacher_attendance_time_ibfk_1` FOREIGN KEY (`school_code`) REFERENCES `schools` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_attendance_time`
--

LOCK TABLES `teacher_attendance_time` WRITE;
/*!40000 ALTER TABLE `teacher_attendance_time` DISABLE KEYS */;
INSERT INTO `teacher_attendance_time` VALUES (1,'06:00:00','13:00:00','YSPM');
/*!40000 ALTER TABLE `teacher_attendance_time` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-02 15:23:57
