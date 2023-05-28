CREATE DATABASE  IF NOT EXISTS `dongles_verwaltung` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dongles_verwaltung`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dongles_verwaltung
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add custom user',6,'add_customuser'),(22,'Can change custom user',6,'change_customuser'),(23,'Can delete custom user',6,'delete_customuser'),(24,'Can view custom user',6,'view_customuser'),(25,'Can view user',6,'can_view_user'),(26,'Can add dongle',7,'add_dongle'),(27,'Can change dongle',7,'change_dongle'),(28,'Can delete dongle',7,'delete_dongle'),(29,'Can view dongle',7,'view_dongle'),(30,'Can add dongle',8,'add_dongle'),(31,'Can change dongle',8,'change_dongle'),(32,'Can delete dongle',8,'delete_dongle'),(33,'Can view dongle',8,'view_dongle'),(34,'Can add kunde',9,'add_kunde'),(35,'Can change kunde',9,'change_kunde'),(36,'Can delete kunde',9,'delete_kunde'),(37,'Can view kunde',9,'view_kunde'),(38,'Can add lizenz',10,'add_lizenz'),(39,'Can change lizenz',10,'change_lizenz'),(40,'Can delete lizenz',10,'delete_lizenz'),(41,'Can view lizenz',10,'view_lizenz'),(42,'Can add lizenz',11,'add_lizenz'),(43,'Can change lizenz',11,'change_lizenz'),(44,'Can delete lizenz',11,'delete_lizenz'),(45,'Can view lizenz',11,'view_lizenz');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_User_loggin_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_User_loggin_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `user_loggin_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(8,'benachrichtigung','dongle'),(9,'benachrichtigung','kunde'),(10,'benachrichtigung','lizenz'),(4,'contenttypes','contenttype'),(7,'homepage','dongle'),(11,'Lizenzseite','lizenz'),(5,'sessions','session'),(6,'User_loggin','customuser');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Lizenzseite','0001_initial','2023-05-28 14:32:39.093011'),(2,'contenttypes','0001_initial','2023-05-28 14:32:39.118653'),(3,'contenttypes','0002_remove_content_type_name','2023-05-28 14:32:39.149390'),(4,'auth','0001_initial','2023-05-28 14:32:39.273775'),(5,'auth','0002_alter_permission_name_max_length','2023-05-28 14:32:39.302301'),(6,'auth','0003_alter_user_email_max_length','2023-05-28 14:32:39.308654'),(7,'auth','0004_alter_user_username_opts','2023-05-28 14:32:39.314754'),(8,'auth','0005_alter_user_last_login_null','2023-05-28 14:32:39.321289'),(9,'auth','0006_require_contenttypes_0002','2023-05-28 14:32:39.324287'),(10,'auth','0007_alter_validators_add_error_messages','2023-05-28 14:32:39.330500'),(11,'auth','0008_alter_user_username_max_length','2023-05-28 14:32:39.336763'),(12,'auth','0009_alter_user_last_name_max_length','2023-05-28 14:32:39.342882'),(13,'auth','0010_alter_group_name_max_length','2023-05-28 14:32:39.355296'),(14,'auth','0011_update_proxy_permissions','2023-05-28 14:32:39.363219'),(15,'auth','0012_alter_user_first_name_max_length','2023-05-28 14:32:39.369954'),(16,'User_loggin','0001_initial','2023-05-28 14:32:39.515382'),(17,'admin','0001_initial','2023-05-28 14:32:39.585370'),(18,'admin','0002_logentry_remove_auto_add','2023-05-28 14:32:39.594068'),(19,'admin','0003_logentry_add_action_flag_choices','2023-05-28 14:32:39.602626'),(20,'benachrichtigung','0001_initial','2023-05-28 14:32:39.614478'),(21,'homepage','0001_initial','2023-05-28 14:32:39.618955'),(22,'sessions','0001_initial','2023-05-28 14:32:39.650662');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dongle`
--

DROP TABLE IF EXISTS `dongle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dongle` (
  `Lfd. Nr.` int NOT NULL,
  `Serien-Nr` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Gueltig von` date NOT NULL,
  `Gueltig bis` date NOT NULL,
  `Projekt/Produkt` varchar(45) NOT NULL,
  `Standort` varchar(45) NOT NULL,
  `Haendler` varchar(45) NOT NULL,
  `Datum letzte Aenderung` date NOT NULL,
  `Datum Erstausgabe` date NOT NULL,
  `Benutzer_Firmcode` varchar(45) NOT NULL,
  PRIMARY KEY (`Lfd. Nr.`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dongle`
--

LOCK TABLES `dongle` WRITE;
/*!40000 ALTER TABLE `dongle` DISABLE KEYS */;
INSERT INTO `dongle` VALUES (41,'252','rama','2023-05-22','2023-05-22','test','berlin','rama','2023-05-22','2023-05-22','');
/*!40000 ALTER TABLE `dongle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lizenz`
--

DROP TABLE IF EXISTS `lizenz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lizenz` (
  `Lfd. Nr.` int NOT NULL,
  `ProductCode` int NOT NULL,
  `LizenzName` varchar(45) NOT NULL,
  `Einheiten` int DEFAULT NULL,
  `Gueltig von` date NOT NULL,
  `Ablaufdatum` date NOT NULL,
  `LizenzAnzahl` int NOT NULL,
  `Mitarbeiter` varchar(45) NOT NULL,
  `Projekt` varchar(45) NOT NULL,
  `dongle_Lfd. Nr.` int NOT NULL,
  PRIMARY KEY (`Lfd. Nr.`),
  KEY `fk_lizenz_dongle1_idx` (`dongle_Lfd. Nr.`),
  CONSTRAINT `fk_lizenz_dongle1` FOREIGN KEY (`dongle_Lfd. Nr.`) REFERENCES `dongle` (`Lfd. Nr.`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lizenz`
--

LOCK TABLES `lizenz` WRITE;
/*!40000 ALTER TABLE `lizenz` DISABLE KEYS */;
/*!40000 ALTER TABLE `lizenz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `ID_Ticket` int NOT NULL,
  `Titel` varchar(45) NOT NULL,
  `Beschreibung` varchar(45) NOT NULL,
  `Status` varchar(45) NOT NULL,
  `Erstellungsdatum` date NOT NULL,
  `Schliessungsdatum` date DEFAULT NULL,
  `Admin/Verwalter_ID` int DEFAULT NULL,
  `dongle_Lfd. Nr.` int NOT NULL,
  KEY `fk_ticket_dongle1_idx` (`dongle_Lfd. Nr.`),
  CONSTRAINT `fk_ticket_dongle1` FOREIGN KEY (`dongle_Lfd. Nr.`) REFERENCES `dongle` (`Lfd. Nr.`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_loggin_customuser`
--

DROP TABLE IF EXISTS `user_loggin_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_loggin_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `username` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(10) NOT NULL,
  `firm_code` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_loggin_customuser`
--

LOCK TABLES `user_loggin_customuser` WRITE;
/*!40000 ALTER TABLE `user_loggin_customuser` DISABLE KEYS */;
INSERT INTO `user_loggin_customuser` VALUES (1,NULL,0,'admin@example.com','default_username','Admin User','pbkdf2_sha256$600000$KI8s1w4TrDfG5Da6bekdEe$J81L6x/yiMzRgWrszK/iTgJUHMPxlySmroBDLID2Gsw=','Admin',NULL,1,0),(2,NULL,0,'newuser@example.com','default_username','New User','pbkdf2_sha256$600000$ah7i3YnMg1rAALChP85DCz$aDMwX42235kTw+HGopCom6nyHlOHPnNQiD13u+EXovQ=','Verwalter',NULL,1,0),(3,NULL,0,'kundeuser@example.com','default_username','Kunde User','pbkdf2_sha256$600000$fDcpbGPQ1M0dnYzKPcrJzd$ry8pHNrVSrrKwxxU8wCZo8RaeHAwJkQqeGIq2Dv3Izg=','Kunde','FIRM123',1,0);
/*!40000 ALTER TABLE `user_loggin_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_loggin_customuser_groups`
--

DROP TABLE IF EXISTS `user_loggin_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_loggin_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_loggin_customuser_g_customuser_id_group_id_138a3e59_uniq` (`customuser_id`,`group_id`),
  KEY `User_loggin_customuser_groups_group_id_de373d02_fk_auth_group_id` (`group_id`),
  CONSTRAINT `User_loggin_customus_customuser_id_002b76a8_fk_User_logg` FOREIGN KEY (`customuser_id`) REFERENCES `user_loggin_customuser` (`id`),
  CONSTRAINT `User_loggin_customuser_groups_group_id_de373d02_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_loggin_customuser_groups`
--

LOCK TABLES `user_loggin_customuser_groups` WRITE;
/*!40000 ALTER TABLE `user_loggin_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_loggin_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_loggin_customuser_user_permissions`
--

DROP TABLE IF EXISTS `user_loggin_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_loggin_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_loggin_customuser_u_customuser_id_permission_9b53ae07_uniq` (`customuser_id`,`permission_id`),
  KEY `User_loggin_customus_permission_id_b5493b82_fk_auth_perm` (`permission_id`),
  CONSTRAINT `User_loggin_customus_customuser_id_702e1faf_fk_User_logg` FOREIGN KEY (`customuser_id`) REFERENCES `user_loggin_customuser` (`id`),
  CONSTRAINT `User_loggin_customus_permission_id_b5493b82_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_loggin_customuser_user_permissions`
--

LOCK TABLES `user_loggin_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `user_loggin_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_loggin_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-28 16:43:56
