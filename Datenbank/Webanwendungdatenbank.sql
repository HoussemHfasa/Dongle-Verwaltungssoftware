CREATE DATABASE  IF NOT EXISTS `donglewebanwendung` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `donglewebanwendung`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: donglewebanwendung
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
-- Table structure for table `admin_verwalter`
--

DROP TABLE IF EXISTS `admin_verwalter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_verwalter` (
  `ID` int NOT NULL,
  `Name` varchar(45) NOT NULL,
  `E-mail` varchar(45) NOT NULL,
  `Passwort` varchar(45) NOT NULL,
  `Rolle` enum('Admin','Verwalter') NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_verwalter`
--

LOCK TABLES `admin_verwalter` WRITE;
/*!40000 ALTER TABLE `admin_verwalter` DISABLE KEYS */;
INSERT INTO `admin_verwalter` VALUES (1,'Houssem','Houssem.Hfasa@Student.HTW-Berlin.de','houssem123','Admin'),(2,'yassin','yassin@gmail.com','y123','Verwalter');
/*!40000 ALTER TABLE `admin_verwalter` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add kunde',7,'add_kunde'),(26,'Can change kunde',7,'change_kunde'),(27,'Can delete kunde',7,'delete_kunde'),(28,'Can view kunde',7,'view_kunde'),(29,'Can add admin_verwalter',8,'add_admin_verwalter'),(30,'Can change admin_verwalter',8,'change_admin_verwalter'),(31,'Can delete admin_verwalter',8,'delete_admin_verwalter'),(32,'Can view admin_verwalter',8,'view_admin_verwalter'),(33,'Can add Token',9,'add_token'),(34,'Can change Token',9,'change_token'),(35,'Can delete Token',9,'delete_token'),(36,'Can view Token',9,'view_token'),(37,'Can add token',10,'add_tokenproxy'),(38,'Can change token',10,'change_tokenproxy'),(39,'Can delete token',10,'delete_tokenproxy'),(40,'Can view token',10,'view_tokenproxy');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$600000$fcMlZlID9wRnCqBq6NL58o$IQ0HleBky8CcVY8qtIDtcWOudzZmF3HZ74B3z2hGxRU=',NULL,1,'Houssem','','','Houssem.Hfasa@student.htw-berlin.de',1,1,'2023-05-18 21:54:52.951523');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
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
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'authtoken','token'),(10,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'users','admin_verwalter'),(7,'users','kunde');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-05-14 10:08:38.432996'),(2,'auth','0001_initial','2023-05-14 10:08:38.717361'),(3,'admin','0001_initial','2023-05-14 10:08:38.792502'),(4,'admin','0002_logentry_remove_auto_add','2023-05-14 10:08:38.800710'),(5,'admin','0003_logentry_add_action_flag_choices','2023-05-14 10:08:38.808274'),(6,'contenttypes','0002_remove_content_type_name','2023-05-14 10:08:38.855614'),(7,'auth','0002_alter_permission_name_max_length','2023-05-14 10:08:38.889260'),(8,'auth','0003_alter_user_email_max_length','2023-05-14 10:08:38.927395'),(9,'auth','0004_alter_user_username_opts','2023-05-14 10:08:38.936265'),(10,'auth','0005_alter_user_last_login_null','2023-05-14 10:08:38.969299'),(11,'auth','0006_require_contenttypes_0002','2023-05-14 10:08:38.972739'),(12,'auth','0007_alter_validators_add_error_messages','2023-05-14 10:08:38.979315'),(13,'auth','0008_alter_user_username_max_length','2023-05-14 10:08:39.017145'),(14,'auth','0009_alter_user_last_name_max_length','2023-05-14 10:08:39.056392'),(15,'auth','0010_alter_group_name_max_length','2023-05-14 10:08:39.087321'),(16,'auth','0011_update_proxy_permissions','2023-05-14 10:08:39.095325'),(17,'auth','0012_alter_user_first_name_max_length','2023-05-14 10:08:39.135386'),(18,'sessions','0001_initial','2023-05-14 10:08:39.159333'),(19,'authtoken','0001_initial','2023-05-18 18:55:06.607667'),(20,'authtoken','0002_auto_20160226_1747','2023-05-18 18:55:06.626606'),(21,'authtoken','0003_tokenproxy','2023-05-18 18:55:06.630633'),(22,'users','0001_initial','2023-05-18 18:55:06.961665');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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
  `Gültig von` date NOT NULL,
  `Gültig bis` date NOT NULL,
  `Projekt/Produkt` varchar(45) NOT NULL,
  `Standort` varchar(45) NOT NULL,
  `Händler` varchar(45) NOT NULL,
  `Datum letzte Änderung` date NOT NULL,
  `Datum Erstausgabe` date NOT NULL,
  `Benutzer_Firmcode` int NOT NULL,
  PRIMARY KEY (`Lfd. Nr.`,`Benutzer_Firmcode`),
  KEY `fk_Dognle_Benutzer1_idx` (`Benutzer_Firmcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dongle`
--

LOCK TABLES `dongle` WRITE;
/*!40000 ALTER TABLE `dongle` DISABLE KEYS */;
INSERT INTO `dongle` VALUES (41,'252','rama','2023-05-22','2023-05-22','test','berlin','rama','2023-05-22','2023-05-22',514584);
/*!40000 ALTER TABLE `dongle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kunde`
--

DROP TABLE IF EXISTS `kunde`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kunde` (
  `Firmcode` int NOT NULL,
  `Name` varchar(45) NOT NULL,
  `E-mail` varchar(45) NOT NULL,
  `Passwort` varchar(45) NOT NULL,
  PRIMARY KEY (`Firmcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kunde`
--

LOCK TABLES `kunde` WRITE;
/*!40000 ALTER TABLE `kunde` DISABLE KEYS */;
INSERT INTO `kunde` VALUES (514584,'rama','rama','rama');
/*!40000 ALTER TABLE `kunde` ENABLE KEYS */;
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
  `Gültig von` date NOT NULL,
  `Ablaufdatum` date NOT NULL,
  `LizenzAnzahl` int NOT NULL,
  `Mitarbeiter` varchar(45) NOT NULL,
  `Projekt` varchar(45) NOT NULL,
  `Dognle_Lfd. Nr.` int NOT NULL,
  PRIMARY KEY (`Lfd. Nr.`,`Dognle_Lfd. Nr.`),
  KEY `fk_Lizenz_Dognle_idx` (`Dognle_Lfd. Nr.`)
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
  `Schließungsdatum` date NOT NULL,
  `Admin/Verwalter_ID` int NOT NULL,
  `Dognle_Lfd. Nr.` int NOT NULL,
  `Dognle_Benutzer_Firmcode` int NOT NULL,
  `Benutzer_Firmcode` int NOT NULL,
  PRIMARY KEY (`ID_Ticket`,`Admin/Verwalter_ID`,`Dognle_Lfd. Nr.`,`Dognle_Benutzer_Firmcode`,`Benutzer_Firmcode`),
  KEY `fk_Ticket_Admin/Verwalter1_idx` (`Admin/Verwalter_ID`),
  KEY `fk_Ticket_Dognle1_idx` (`Dognle_Lfd. Nr.`,`Dognle_Benutzer_Firmcode`),
  KEY `fk_Ticket_Benutzer1_idx` (`Benutzer_Firmcode`),
  CONSTRAINT `fk_Ticket_Admin/Verwalter1` FOREIGN KEY (`Admin/Verwalter_ID`) REFERENCES `admin_verwalter` (`ID`)
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
-- Table structure for table `users_admin_verwalter`
--

DROP TABLE IF EXISTS `users_admin_verwalter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_admin_verwalter` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_admin_verwalter`
--

LOCK TABLES `users_admin_verwalter` WRITE;
/*!40000 ALTER TABLE `users_admin_verwalter` DISABLE KEYS */;
INSERT INTO `users_admin_verwalter` VALUES (1,NULL,0,'houssemhfasa@gmail.com','','pbkdf2_sha256$600000$CIwtAi8sZ9HQM8nFlZo1db$+HD6O+j4xjKlxpJq8dEEGEG0HO2akuuOnO3JW04pARs=',''),(2,NULL,0,'verwalter@example.com','','pbkdf2_sha256$600000$ti5hFw6ABuI5kxY6YIpody$ZhWpBnusESZbjxT9m7IewHeLKrX580+v2n9DhVpgTF4=',''),(3,NULL,0,'admin@example.com','','pbkdf2_sha256$600000$gb8NehaCx0pMKMuHrptM7Z$r5wXpQNam5uC6yL0G+tGGwYf1Lqjp9oxEpaK5SZMt84=','');
/*!40000 ALTER TABLE `users_admin_verwalter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_admin_verwalter_groups`
--

DROP TABLE IF EXISTS `users_admin_verwalter_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_admin_verwalter_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin_verwalter_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_admin_verwalter_gr_admin_verwalter_id_group_ea709c81_uniq` (`admin_verwalter_id`,`group_id`),
  KEY `users_admin_verwalter_groups_group_id_fff1af7f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_admin_verwalte_admin_verwalter_id_6e92b72e_fk_users_adm` FOREIGN KEY (`admin_verwalter_id`) REFERENCES `users_admin_verwalter` (`id`),
  CONSTRAINT `users_admin_verwalter_groups_group_id_fff1af7f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_admin_verwalter_groups`
--

LOCK TABLES `users_admin_verwalter_groups` WRITE;
/*!40000 ALTER TABLE `users_admin_verwalter_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_admin_verwalter_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_admin_verwalter_user_permissions`
--

DROP TABLE IF EXISTS `users_admin_verwalter_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_admin_verwalter_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin_verwalter_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_admin_verwalter_us_admin_verwalter_id_permi_7219a304_uniq` (`admin_verwalter_id`,`permission_id`),
  KEY `users_admin_verwalte_permission_id_2554d57a_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_admin_verwalte_admin_verwalter_id_bb83107a_fk_users_adm` FOREIGN KEY (`admin_verwalter_id`) REFERENCES `users_admin_verwalter` (`id`),
  CONSTRAINT `users_admin_verwalte_permission_id_2554d57a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_admin_verwalter_user_permissions`
--

LOCK TABLES `users_admin_verwalter_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_admin_verwalter_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_admin_verwalter_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_kunde`
--

DROP TABLE IF EXISTS `users_kunde`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_kunde` (
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `firmcode` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`firmcode`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_kunde`
--

LOCK TABLES `users_kunde` WRITE;
/*!40000 ALTER TABLE `users_kunde` DISABLE KEYS */;
INSERT INTO `users_kunde` VALUES (NULL,0,'','','kunde@example.com','pbkdf2_sha256$600000$oWAmZvUNEPltMyHkM2eqMf$Xj4Be875yVJ+zw0MJUk9WPcppgHm17c8WDUEbkjsbXQ=');
/*!40000 ALTER TABLE `users_kunde` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_kunde_groups`
--

DROP TABLE IF EXISTS `users_kunde_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_kunde_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kunde_id` varchar(255) NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_kunde_groups_kunde_id_group_id_86e3f382_uniq` (`kunde_id`,`group_id`),
  KEY `users_kunde_groups_group_id_e98bb91a_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_kunde_groups_group_id_e98bb91a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_kunde_groups_kunde_id_01e19074_fk_users_kunde_firmcode` FOREIGN KEY (`kunde_id`) REFERENCES `users_kunde` (`firmcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_kunde_groups`
--

LOCK TABLES `users_kunde_groups` WRITE;
/*!40000 ALTER TABLE `users_kunde_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_kunde_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_kunde_user_permissions`
--

DROP TABLE IF EXISTS `users_kunde_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_kunde_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kunde_id` varchar(255) NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_kunde_user_permiss_kunde_id_permission_id_c6187b07_uniq` (`kunde_id`,`permission_id`),
  KEY `users_kunde_user_per_permission_id_2ea18d79_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_kunde_user_per_kunde_id_806ea125_fk_users_kun` FOREIGN KEY (`kunde_id`) REFERENCES `users_kunde` (`firmcode`),
  CONSTRAINT `users_kunde_user_per_permission_id_2ea18d79_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_kunde_user_permissions`
--

LOCK TABLES `users_kunde_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_kunde_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_kunde_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-22 15:24:58
