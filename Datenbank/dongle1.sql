CREATE DATABASE  IF NOT EXISTS `dongle1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dongle1`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dongle1
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
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add custom user',6,'add_customuser'),(22,'Can change custom user',6,'change_customuser'),(23,'Can delete custom user',6,'delete_customuser'),(24,'Can view custom user',6,'view_customuser'),(25,'Can view user',6,'can_view_user'),(26,'Can add dongle',7,'add_dongle'),(27,'Can change dongle',7,'change_dongle'),(28,'Can delete dongle',7,'delete_dongle'),(29,'Can view dongle',7,'view_dongle'),(30,'Can add dongle',8,'add_dongle'),(31,'Can change dongle',8,'change_dongle'),(32,'Can delete dongle',8,'delete_dongle'),(33,'Can view dongle',8,'view_dongle'),(34,'Can add kunde',9,'add_kunde'),(35,'Can change kunde',9,'change_kunde'),(36,'Can delete kunde',9,'delete_kunde'),(37,'Can view kunde',9,'view_kunde'),(38,'Can add lizenz',10,'add_lizenz'),(39,'Can change lizenz',10,'change_lizenz'),(40,'Can delete lizenz',10,'delete_lizenz'),(41,'Can view lizenz',10,'view_lizenz'),(42,'Can add lizenz',11,'add_lizenz'),(43,'Can change lizenz',11,'change_lizenz'),(44,'Can delete lizenz',11,'delete_lizenz'),(45,'Can view lizenz',11,'view_lizenz'),(46,'Can add user loggin customuser',12,'add_userloggincustomuser'),(47,'Can change user loggin customuser',12,'change_userloggincustomuser'),(48,'Can delete user loggin customuser',12,'delete_userloggincustomuser'),(49,'Can view user loggin customuser',12,'view_userloggincustomuser'),(50,'Can add customuser',13,'add_customuser'),(51,'Can change customuser',13,'change_customuser'),(52,'Can delete customuser',13,'delete_customuser'),(53,'Can view customuser',13,'view_customuser'),(54,'Can add dongle',14,'add_dongle'),(55,'Can change dongle',14,'change_dongle'),(56,'Can delete dongle',14,'delete_dongle'),(57,'Can view dongle',14,'view_dongle'),(58,'Can add user loggin customuser',15,'add_userloggincustomuser'),(59,'Can change user loggin customuser',15,'change_userloggincustomuser'),(60,'Can delete user loggin customuser',15,'delete_userloggincustomuser'),(61,'Can view user loggin customuser',15,'view_userloggincustomuser'),(62,'Can add dongle',16,'add_dongle'),(63,'Can change dongle',16,'change_dongle'),(64,'Can delete dongle',16,'delete_dongle'),(65,'Can view dongle',16,'view_dongle'),(66,'Can add lizenz',17,'add_lizenz'),(67,'Can change lizenz',17,'change_lizenz'),(68,'Can delete lizenz',17,'delete_lizenz'),(69,'Can view lizenz',17,'view_lizenz'),(70,'Can add user loggin customuser',18,'add_userloggincustomuser'),(71,'Can change user loggin customuser',18,'change_userloggincustomuser'),(72,'Can delete user loggin customuser',18,'delete_userloggincustomuser'),(73,'Can view user loggin customuser',18,'view_userloggincustomuser'),(74,'Can add ticket',19,'add_ticket'),(75,'Can change ticket',19,'change_ticket'),(76,'Can delete ticket',19,'delete_ticket'),(77,'Can view ticket',19,'view_ticket'),(78,'Can add lizenz',20,'add_lizenz'),(79,'Can change lizenz',20,'change_lizenz'),(80,'Can delete lizenz',20,'delete_lizenz'),(81,'Can view lizenz',20,'view_lizenz'),(82,'Can add ticket',21,'add_ticket'),(83,'Can change ticket',21,'change_ticket'),(84,'Can delete ticket',21,'delete_ticket'),(85,'Can view ticket',21,'view_ticket');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-06-18 11:03:25.256144','24','inessbouazizi2@gmail.com',2,'[{\"changed\": {\"fields\": [\"Is superuser\"]}}]',6,1),(2,'2023-06-18 11:53:11.256191','24','inessbouazizi2@gmail.com',3,'',6,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(13,'Adminseite','customuser'),(3,'auth','group'),(2,'auth','permission'),(8,'benachrichtigung','dongle'),(9,'benachrichtigung','kunde'),(10,'benachrichtigung','lizenz'),(12,'benachrichtigung','userloggincustomuser'),(4,'contenttypes','contenttype'),(14,'Dongle_hinzufügen','dongle'),(15,'Dongle_hinzufügen','userloggincustomuser'),(21,'DongleAnfordern','ticket'),(7,'homepage','dongle'),(20,'LizenzAnfordern','lizenz'),(19,'LizenzAnfordern','ticket'),(16,'Lizenzhinzufügen','dongle'),(17,'Lizenzhinzufügen','lizenz'),(18,'Lizenzhinzufügen','userloggincustomuser'),(11,'Lizenzseite','lizenz'),(5,'sessions','session'),(6,'User_loggin','customuser');
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
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Lizenzseite','0001_initial','2023-05-28 14:32:39.093011'),(2,'contenttypes','0001_initial','2023-05-28 14:32:39.118653'),(3,'contenttypes','0002_remove_content_type_name','2023-05-28 14:32:39.149390'),(4,'auth','0001_initial','2023-05-28 14:32:39.273775'),(5,'auth','0002_alter_permission_name_max_length','2023-05-28 14:32:39.302301'),(6,'auth','0003_alter_user_email_max_length','2023-05-28 14:32:39.308654'),(7,'auth','0004_alter_user_username_opts','2023-05-28 14:32:39.314754'),(8,'auth','0005_alter_user_last_login_null','2023-05-28 14:32:39.321289'),(9,'auth','0006_require_contenttypes_0002','2023-05-28 14:32:39.324287'),(10,'auth','0007_alter_validators_add_error_messages','2023-05-28 14:32:39.330500'),(11,'auth','0008_alter_user_username_max_length','2023-05-28 14:32:39.336763'),(12,'auth','0009_alter_user_last_name_max_length','2023-05-28 14:32:39.342882'),(13,'auth','0010_alter_group_name_max_length','2023-05-28 14:32:39.355296'),(14,'auth','0011_update_proxy_permissions','2023-05-28 14:32:39.363219'),(15,'auth','0012_alter_user_first_name_max_length','2023-05-28 14:32:39.369954'),(16,'User_loggin','0001_initial','2023-05-28 14:32:39.515382'),(17,'admin','0001_initial','2023-05-28 14:32:39.585370'),(18,'admin','0002_logentry_remove_auto_add','2023-05-28 14:32:39.594068'),(19,'admin','0003_logentry_add_action_flag_choices','2023-05-28 14:32:39.602626'),(20,'benachrichtigung','0001_initial','2023-05-28 14:32:39.614478'),(21,'homepage','0001_initial','2023-05-28 14:32:39.618955'),(22,'sessions','0001_initial','2023-05-28 14:32:39.650662'),(23,'User_loggin','0002_alter_customuser_options','2023-06-08 11:14:13.491526'),(24,'benachrichtigung','0002_userloggincustomuser_delete_kunde','2023-06-08 11:14:13.497799'),(25,'Adminseite','0001_initial','2023-06-08 22:48:09.248610'),(26,'User_loggin','0003_alter_customuser_table','2023-06-08 22:48:09.259755'),(27,'Adminseite','0002_alter_customuser_table','2023-06-08 22:49:04.570268'),(28,'Dongle_hinzufügen','0001_initial','2023-06-11 21:53:33.828163'),(29,'Lizenzhinzufügen','0001_initial','2023-06-26 16:08:22.967333'),(30,'LizenzAnfordern','0001_initial','2023-07-04 14:30:32.905564'),(31,'LizenzAnfordern','0002_lizenz','2023-07-05 13:50:59.068621'),(32,'User_loggin','0004_alter_customuser_options','2023-07-05 14:44:10.765918'),(33,'Dongle_hinzufügen','0002_delete_userloggincustomuser_alter_dongle_options','2023-07-05 19:51:59.872261'),(34,'Lizenzhinzufügen','0002_delete_dongle_delete_userloggincustomuser_and_more','2023-07-05 20:06:24.893021'),(35,'Adminseite','0003_delete_customuser','2023-07-07 11:13:23.946312'),(36,'DongleAnfordern','0001_initial','2023-07-07 11:13:23.952387');
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
INSERT INTO `django_session` VALUES ('psmg47728u7aqa9ezywhf7um6xx0xcng','.eJxVjM0OwiAQhN-FsyFLF0E8eu8zkF1-pGogKe3J-O62SQ96m8z3zbyFp3Upfu1p9lMUV6HE6bdjCs9UdxAfVO9NhlaXeWK5K_KgXY4tptftcP8OCvWyrSGdrUt4yTG7zA60MyoDozOknWWFZmAFOqNWQQczAFqCLXKCbCOh-HwB0lg3aA:1qAVVT:H61MV9JFwH4TJXmzxxKL7sMkYzazxj8LTwVtk0nojIg','2023-07-01 12:58:19.189713');
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
  `Gueltig von` date DEFAULT NULL,
  `Gueltig bis` date DEFAULT NULL,
  `Projekt/Produkt` varchar(45) NOT NULL,
  `Kunde` varchar(45) NOT NULL,
  `Standort` varchar(45) NOT NULL,
  `Haendler` varchar(45) DEFAULT NULL,
  `Datum letzte Aenderung` date NOT NULL,
  `Datum Erstausgabe` date NOT NULL,
  `Firmcode` varchar(45) NOT NULL,
  PRIMARY KEY (`Lfd. Nr.`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dongle`
--

LOCK TABLES `dongle` WRITE;
/*!40000 ALTER TABLE `dongle` DISABLE KEYS */;
INSERT INTO `dongle` VALUES (1,'5-1234567','Testdongle					',NULL,NULL,'intern','GFal','a',NULL,'2019-01-01','2020-02-27',''),(2,'6-8889998','Dongle Berlin					',NULL,NULL,'SW A','Firma Z','Hamburg',NULL,'2019-09-01','2019-09-27',''),(8,'6571232	','Dongle Dresden',NULL,'2023-06-30','SW K','Kunde User','a',NULL,'2020-11-01','2020-11-01','FIRM123'),(9,'5165','Mic','2023-10-20','2023-10-21','SW A','Kunde User','Berlin','Gfal','2023-06-13','2023-09-20','FIRM123'),(10,'1-458794','Mic','2023-06-12','2023-06-17','SW A','Kunde User','Berlin','3asfour','2023-06-13','2023-06-13','FIRM123'),(11,'5645313','fgdfg','2023-06-22','2023-06-21','dfgdfg','Kunde User','dfgdfg','dfgfdg','2023-06-17','2023-06-17','FIRM123'),(12,'6-5848','MC','2023-05-29','2023-06-29','SW A','Kunde User','Berlin','MC','2023-06-18','2023-06-18','FIRM123'),(15,'452425','fghbfg','2023-06-01','2023-06-29','fdgdf','HoussemKunde122','fgb','fgbx','2023-06-18','2023-06-18','dsfdsf5113'),(16,'51561','SA','2023-06-13','2023-06-29','SW','Kundetest','Berlin','GFAL','2023-06-20','2023-06-20','HTWK'),(17,'51561','test after tests','2023-06-27','2023-07-14','dvfdvb','Kunde User','dfbdfb','dfbdfb','2023-07-05','2023-07-05','FIRM123'),(18,'6546','test after Adminseite','2023-07-11','2023-08-02','sgdsfg','Kunde User','dbfb','dfbfdb','2023-07-05','2023-07-05','FIRM123'),(19,'4574','test ende 0507','2023-06-28','2023-07-12','dfbfd','Kunde User','dfbdfb','dfbdfb','2023-07-05','2023-07-05','FIRM123');
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
  `FirmCode` varchar(45) NOT NULL,
  `ProductCode` int NOT NULL,
  `LizenzName` varchar(45) NOT NULL,
  `Einheiten` int DEFAULT NULL,
  `Gueltig von` date NOT NULL,
  `Gueltig bis` date DEFAULT NULL,
  `LizenzAnzahl` int DEFAULT NULL,
  `Mitarbeiter` varchar(45) NOT NULL,
  `Projekt` varchar(45) NOT NULL,
  `Kunde` varchar(45) NOT NULL,
  `Dongle_Serien-Nr` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Lfd. Nr.`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lizenz`
--

LOCK TABLES `lizenz` WRITE;
/*!40000 ALTER TABLE `lizenz` DISABLE KEYS */;
INSERT INTO `lizenz` VALUES (1,'101758',41000,'Hauptmodul',1,'2019-09-27',NULL,NULL,'D. Elgnod','SW A','Firma Z','6-8889998'),(2,'101758',41103,'Modul 1',1,'2019-09-27',NULL,NULL,'D. Elgnod','SW A','Firma Z',NULL),(3,'101758',41160,'Modul 3',1,'2019-09-27',NULL,NULL,'D. Elgnod','SW A','Firma Z',NULL),(4,'101758',41300,'Algorithmus Add',1,'2019-09-27',NULL,NULL,'D. Elgnod','SW A','Firma Z',NULL),(5,'101758',41487,'Algorithmus Sub',1,'2019-09-27',NULL,NULL,'D. Elgnod','SW A','Firma Z',NULL),(6,'FIRM123',41489,'Algorithmus Sub',1,'2019-09-27',NULL,NULL,'D. Elgnod','SW A','Kunde User',NULL),(7,'FIRM123',4524,'fghfgh',2,'2023-06-01','2023-06-14',4,'hgfhfg','sdfsd','Kunde User',''),(8,'FIRM123',4532,'sdfsd',4,'2023-06-22','2023-06-29',7,'dsfsdf','fgshf','Kunde User','6-5848'),(9,'FIRM123',42,'fgngf',45,'2023-06-01','2023-06-29',4,'fngn','fghgfh','Kunde User','1-458794'),(10,'HTWK',6515,'djvhbdshvb',5,'2023-08-02','2023-08-05',2,'jhdbsvhsd','sdvsd','Kundetest',''),(11,'HTWK',154,'dfbdfb',2,'2023-07-04','2023-07-21',3,'dgfbd','dfbdb','Kundetest',''),(12,'FIRM123',5254,'dfbfdb',4,'2023-06-28','2023-07-12',7,'fdvdfb','fdbdfb','Kunde User',''),(13,'FIRM123',452,'dfbfdb',74,'2023-06-26','2023-07-24',2,'fdbfdb','fgnfgn','Kunde User','4574');
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
  `Dongle/Lizenz` tinyint(1) DEFAULT NULL,
  `Dongle_Name` varchar(45) DEFAULT NULL,
  `Dongle_seriennumemr` varchar(45) DEFAULT NULL,
  `LizenzName` varchar(45) DEFAULT NULL,
  `Firmcode` varchar(45) NOT NULL,
  `Gueltig von` date DEFAULT NULL,
  `Gueltig bis` date DEFAULT NULL,
  `Einheiten` int DEFAULT NULL,
  `Projekt` varchar(45) DEFAULT NULL,
  `Grund_der_Ablehnung` varchar(45) DEFAULT NULL,
  `Admin/Verwalter_Email` varchar(45) DEFAULT NULL,
  `Händler` varchar(45) DEFAULT NULL,
  `Standort` varchar(45) NOT NULL,
  PRIMARY KEY (`ID_Ticket`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (1,'ebdf','dhbdfb','offen','2019-09-27','2019-09-27',NULL,NULL,NULL,NULL,'FIRM123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'');
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
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(10) NOT NULL,
  `firm_code` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `idx_user_loggin_customuser_firm_code` (`firm_code`),
  CONSTRAINT `chk_role_values` CHECK ((`role` in (_utf8mb4'Admin',_utf8mb4'Verwalter',_utf8mb4'Kunde')))
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_loggin_customuser`
--

LOCK TABLES `user_loggin_customuser` WRITE;
/*!40000 ALTER TABLE `user_loggin_customuser` DISABLE KEYS */;
INSERT INTO `user_loggin_customuser` VALUES (1,'2023-06-17 12:58:19.185166',1,'admin@example.com','Admin User','pbkdf2_sha256$600000$i4pYEftS29PpAHx8Za46td$SS2tXduzLFPWWWgVCralmZMscr76/oTLT9JYOYEWHm4=','Admin',NULL),(2,'2023-07-05 21:47:23.034682',0,'newuser@example.com','New User','pbkdf2_sha256$600000$RL3bhLGOg2KRiijBSLTv6c$O2bnZQ4wG3KLe7+GDDydcZa5L7CtQ0lMWlQImp8cxio=','Verwalter',NULL),(3,'2023-07-05 14:28:50.941846',0,'kundeuser@example.com','Kunde User','pbkdf2_sha256$600000$wUycAMTZQYZIeyanzi6dtg$yfj/SmebaTZxxo5Btmc4x/PAJWuNwjkUwPtdNHvtlKo=','Kunde','FIRM123'),(5,NULL,0,'firmaz@example.com','Firma Z','testpassword','Kunde','101758'),(8,NULL,0,'houssemhfasa2@gmail.com','Houssemkunde','pbkdf2_sha256$600000$dE4tLLNsyOt07RYd3SdcqC$VSRAdBzxC8xNA1I6NfGYKIW5rWPGdJ3EuWgBKesi64A=','Kunde','18'),(20,NULL,1,'houssemhfasa@gmail.com','houssem147','pbkdf2_sha256$600000$RGiKrESbXXTo3OqPbLx5Lk$cQfywAukFYpQMmEHKkVBCSFBv6+XAsJsmuVn0rlh+ig=','Admin',''),(21,NULL,1,'houssemhfassa28@gmail.com','houssemrandom','pbkdf2_sha256$600000$Ju1EPuZYJrKdXharcyILEZ$1h83KYegTE+ugxZNqKqOiG3cllmYeS4oF8VQjmCWXfA=','Admin',''),(22,NULL,0,'houssemhfassa25@gmail.com','Verwalter Test','pbkdf2_sha256$600000$1WcqEdiT8aBbKUw6V0JePK$mZoud8rKtTeO3VRavEZFJmsbsLnUBynq04olicXuLBE=','Verwalter',''),(30,NULL,0,'houssemhfassa36@gmail.com','HoussemKunde122','pbkdf2_sha256$600000$BUUHvKLq6cCa12umtcIlVm$C3GhaC+pTLBd+KWUou6pSilw90G+jenEfqIXBYj5uG8=','Kunde','dsfdsf5113'),(32,NULL,0,'houssemhfassa48@gmail.com','dfbfdb','pbkdf2_sha256$600000$4FiRHW0xbhRNVXDpLhgb8w$Jifyg7y9C8KVKoxXPIN22DI4yWtAX/icBugXKXiWdXA=','Verwalter',''),(33,'2023-07-04 14:14:07.829373',0,'kundehtw@gmail.com','Kundetest','pbkdf2_sha256$600000$LMltFqjz3K0VSCyEAKq39I$+PaIm1jOZt6l0ZC7IGEnE3YTCalH58VNOmH+bPReAYk=','Kunde','HTWK');
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

-- Dump completed on 2023-07-07 14:17:35
