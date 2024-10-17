-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: Conaldex_Boyaca
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add Categoria',6,'add_categoria'),(22,'Can change Categoria',6,'change_categoria'),(23,'Can delete Categoria',6,'delete_categoria'),(24,'Can view Categoria',6,'view_categoria'),(25,'Can add Compra',7,'add_compras'),(26,'Can change Compra',7,'change_compras'),(27,'Can delete Compra',7,'delete_compras'),(28,'Can view Compra',7,'view_compras'),(29,'Can add Departamento',8,'add_departamentos'),(30,'Can change Departamento',8,'change_departamentos'),(31,'Can delete Departamento',8,'delete_departamentos'),(32,'Can view Departamento',8,'view_departamentos'),(33,'Can add Proveedor',9,'add_proveedor'),(34,'Can change Proveedor',9,'change_proveedor'),(35,'Can delete Proveedor',9,'delete_proveedor'),(36,'Can view Proveedor',9,'view_proveedor'),(37,'Can add Tipo',10,'add_tipo'),(38,'Can change Tipo',10,'change_tipo'),(39,'Can delete Tipo',10,'delete_tipo'),(40,'Can view Tipo',10,'view_tipo'),(41,'Can add Usuarios',11,'add_customuser'),(42,'Can change Usuarios',11,'change_customuser'),(43,'Can delete Usuarios',11,'delete_customuser'),(44,'Can view Usuarios',11,'view_customuser'),(45,'Can add Municipio',12,'add_municipios'),(46,'Can change Municipio',12,'change_municipios'),(47,'Can delete Municipio',12,'delete_municipios'),(48,'Can view Municipio',12,'view_municipios'),(49,'Can add Producto',13,'add_producto'),(50,'Can change Producto',13,'change_producto'),(51,'Can delete Producto',13,'delete_producto'),(52,'Can view Producto',13,'view_producto'),(53,'Can add Normativa',14,'add_normativa'),(54,'Can change Normativa',14,'change_normativa'),(55,'Can delete Normativa',14,'delete_normativa'),(56,'Can view Normativa',14,'view_normativa'),(57,'Can add Detalle de Compra',15,'add_detallecompra'),(58,'Can change Detalle de Compra',15,'change_detallecompra'),(59,'Can delete Detalle de Compra',15,'delete_detallecompra'),(60,'Can view Detalle de Compra',15,'view_detallecompra'),(61,'Can add Stock',16,'add_stock'),(62,'Can change Stock',16,'change_stock'),(63,'Can delete Stock',16,'delete_stock'),(64,'Can view Stock',16,'view_stock'),(65,'Can add Ubicación',17,'add_ubicacion'),(66,'Can change Ubicación',17,'change_ubicacion'),(67,'Can delete Ubicación',17,'delete_ubicacion'),(68,'Can view Ubicación',17,'view_ubicacion'),(69,'Can add Cliente',18,'add_cliente'),(70,'Can change Cliente',18,'change_cliente'),(71,'Can delete Cliente',18,'delete_cliente'),(72,'Can view Cliente',18,'view_cliente'),(73,'Can add Venta',19,'add_venta'),(74,'Can change Venta',19,'change_venta'),(75,'Can delete Venta',19,'delete_venta'),(76,'Can view Venta',19,'view_venta'),(77,'Can add Detalle de Venta',20,'add_detalleventa'),(78,'Can change Detalle de Venta',20,'change_detalleventa'),(79,'Can delete Detalle de Venta',20,'delete_detalleventa'),(80,'Can view Detalle de Venta',20,'view_detalleventa');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Prueba Backup','Esto es una prueba de bakcups.');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_persona` varchar(2) NOT NULL,
  `nombres` varchar(100) DEFAULT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` varchar(11) DEFAULT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `direccion` varchar(50) DEFAULT NULL,
  `ciudad_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `correo` (`correo`),
  UNIQUE KEY `numero_documento` (`numero_documento`),
  KEY `Cliente_ciudad_id_23172d5a_fk_ubicacion_id` (`ciudad_id`),
  CONSTRAINT `Cliente_ciudad_id_23172d5a_fk_ubicacion_id` FOREIGN KEY (`ciudad_id`) REFERENCES `ubicacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compras`
--

DROP TABLE IF EXISTS `compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compras` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `num_factura` varchar(20) NOT NULL,
  `fecha_compra` date NOT NULL,
  `proveedor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Compras_proveedor_id_f5416bdf_fk_Proveedor_id` (`proveedor_id`),
  CONSTRAINT `Compras_proveedor_id_f5416bdf_fk_Proveedor_id` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamentos`
--

DROP TABLE IF EXISTS `departamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamentos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamentos`
--

LOCK TABLES `departamentos` WRITE;
/*!40000 ALTER TABLE `departamentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `departamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detallecompra`
--

DROP TABLE IF EXISTS `detallecompra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detallecompra` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `num_factura` varchar(20) DEFAULT NULL,
  `cantidad` int NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `iva` decimal(5,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `compra_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DetalleCompra_compra_id_e9e73390_fk_Compras_id` (`compra_id`),
  KEY `DetalleCompra_producto_id_8de69c74_fk_Producto_id` (`producto_id`),
  CONSTRAINT `DetalleCompra_compra_id_e9e73390_fk_Compras_id` FOREIGN KEY (`compra_id`) REFERENCES `compras` (`id`),
  CONSTRAINT `DetalleCompra_producto_id_8de69c74_fk_Producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detallecompra`
--

LOCK TABLES `detallecompra` WRITE;
/*!40000 ALTER TABLE `detallecompra` DISABLE KEYS */;
/*!40000 ALTER TABLE `detallecompra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalleventa`
--

DROP TABLE IF EXISTS `detalleventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalleventa` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `iva` int unsigned NOT NULL,
  `total` decimal(9,2) NOT NULL,
  `num_factura` varchar(20) DEFAULT NULL,
  `producto_id` bigint NOT NULL,
  `venta_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DetalleVenta_producto_id_a793c5f8_fk_Stock_id` (`producto_id`),
  KEY `DetalleVenta_venta_id_d892a61e_fk_Venta_id` (`venta_id`),
  CONSTRAINT `DetalleVenta_producto_id_a793c5f8_fk_Stock_id` FOREIGN KEY (`producto_id`) REFERENCES `stock` (`id`),
  CONSTRAINT `DetalleVenta_venta_id_d892a61e_fk_Venta_id` FOREIGN KEY (`venta_id`) REFERENCES `venta` (`id`),
  CONSTRAINT `detalleventa_chk_1` CHECK ((`iva` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalleventa`
--

LOCK TABLES `detalleventa` WRITE;
/*!40000 ALTER TABLE `detalleventa` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalleventa` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk_usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`),
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(6,'app','categoria'),(18,'app','cliente'),(7,'app','compras'),(11,'app','customuser'),(8,'app','departamentos'),(15,'app','detallecompra'),(20,'app','detalleventa'),(12,'app','municipios'),(14,'app','normativa'),(13,'app','producto'),(9,'app','proveedor'),(16,'app','stock'),(10,'app','tipo'),(17,'app','ubicacion'),(19,'app','venta'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-15 18:39:49.661409'),(2,'contenttypes','0002_remove_content_type_name','2024-10-15 18:39:49.697349'),(3,'auth','0001_initial','2024-10-15 18:39:49.891549'),(4,'auth','0002_alter_permission_name_max_length','2024-10-15 18:39:49.958408'),(5,'auth','0003_alter_user_email_max_length','2024-10-15 18:39:49.958408'),(6,'auth','0004_alter_user_username_opts','2024-10-15 18:39:49.958408'),(7,'auth','0005_alter_user_last_login_null','2024-10-15 18:39:49.974806'),(8,'auth','0006_require_contenttypes_0002','2024-10-15 18:39:49.977843'),(9,'auth','0007_alter_validators_add_error_messages','2024-10-15 18:39:49.983847'),(10,'auth','0008_alter_user_username_max_length','2024-10-15 18:39:49.987212'),(11,'auth','0009_alter_user_last_name_max_length','2024-10-15 18:39:49.995658'),(12,'auth','0010_alter_group_name_max_length','2024-10-15 18:39:50.008132'),(13,'auth','0011_update_proxy_permissions','2024-10-15 18:39:50.015906'),(14,'auth','0012_alter_user_first_name_max_length','2024-10-15 18:39:50.020126'),(15,'app','0001_initial','2024-10-15 18:39:51.212365'),(16,'admin','0001_initial','2024-10-15 18:39:51.325490'),(17,'admin','0002_logentry_remove_auto_add','2024-10-15 18:39:51.325490'),(18,'admin','0003_logentry_add_action_flag_choices','2024-10-15 18:39:51.343115'),(19,'inicio','0001_initial','2024-10-15 18:39:51.371792'),(20,'inicio','0002_delete_csrftoken','2024-10-15 18:39:51.375378'),(21,'sessions','0001_initial','2024-10-15 18:39:51.408690');
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
INSERT INTO `django_session` VALUES ('lm6enj6xzel5s9tmwevlymjpcfh835nu','.eJxVjMsOwiAQRf-FtSGAPKYu3fcbyMwAUjU0Ke3K-O_apAvd3nPOfYmI21rj1vMSpyQuQovT70bIj9x2kO7YbrPkua3LRHJX5EG7HOeUn9fD_Tuo2Ou3RocWLakMloxhC0GTIe-hwBm5gFOOfUqs0YXAYKxX6HMo2hGgHQbx_gDn2TfU:1t0mfJ:05MMyMb6Nl_g7dwHhvsKGT3S6sOncmcebJCucvQnCbs','2024-10-29 18:53:05.782653'),('q9yoieqhibefb9qn49dpa4y0rpe2dtvh','.eJxVjMsOwiAQRf-FtSFloDxcuvcbCMwwUjU0Ke3K-O_apAvd3nPOfYmYtrXGrZclTiTOAsTpd8sJH6XtgO6p3WaJc1uXKctdkQft8jpTeV4O9--gpl6_ddGZIaiCQDl75Y1XQaMdydmiB6cckyZipYxntgnCCBgYiGBgYzCI9wfs-TgS:1t1UwH:TNBx61vQAhO57zas_k6oz2FaznVzF0Uq5ROyC_VqijA','2024-10-31 18:09:33.474407');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `municipios`
--

DROP TABLE IF EXISTS `municipios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `municipios` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `departamento_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `municipios_departamento_id_93acf47d_fk_departamentos_id` (`departamento_id`),
  CONSTRAINT `municipios_departamento_id_93acf47d_fk_departamentos_id` FOREIGN KEY (`departamento_id`) REFERENCES `departamentos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `municipios`
--

LOCK TABLES `municipios` WRITE;
/*!40000 ALTER TABLE `municipios` DISABLE KEYS */;
/*!40000 ALTER TABLE `municipios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normativa`
--

DROP TABLE IF EXISTS `normativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `normativa` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `decreto` varchar(50) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `decreto` (`decreto`),
  KEY `Normativa_producto_id_be390836_fk_Producto_id` (`producto_id`),
  CONSTRAINT `Normativa_producto_id_be390836_fk_Producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normativa`
--

LOCK TABLES `normativa` WRITE;
/*!40000 ALTER TABLE `normativa` DISABLE KEYS */;
/*!40000 ALTER TABLE `normativa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `categoria_id` bigint NOT NULL,
  `tipo_pro_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Producto_categoria_id_d52b184f_fk_Categoria_id` (`categoria_id`),
  KEY `Producto_tipo_pro_id_40386015_fk_Tipo_id` (`tipo_pro_id`),
  CONSTRAINT `Producto_categoria_id_d52b184f_fk_Categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`),
  CONSTRAINT `Producto_tipo_pro_id_40386015_fk_Tipo_id` FOREIGN KEY (`tipo_pro_id`) REFERENCES `tipo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_persona` varchar(2) NOT NULL,
  `nombres` varchar(100) DEFAULT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` varchar(11) DEFAULT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `direccion` varchar(50) DEFAULT NULL,
  `ciudad_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `correo` (`correo`),
  UNIQUE KEY `numero_documento` (`numero_documento`),
  KEY `Proveedor_ciudad_id_65bec80c_fk_ubicacion_id` (`ciudad_id`),
  CONSTRAINT `Proveedor_ciudad_id_65bec80c_fk_ubicacion_id` FOREIGN KEY (`ciudad_id`) REFERENCES `ubicacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `nombre_pro_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_pro_id` (`nombre_pro_id`),
  CONSTRAINT `Stock_nombre_pro_id_1beafd21_fk_Producto_id` FOREIGN KEY (`nombre_pro_id`) REFERENCES `producto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo`
--

DROP TABLE IF EXISTS `tipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo`
--

LOCK TABLES `tipo` WRITE;
/*!40000 ALTER TABLE `tipo` DISABLE KEYS */;
INSERT INTO `tipo` VALUES (1,'Pruebaaa','Pruebaa12');
/*!40000 ALTER TABLE `tipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubicacion`
--

DROP TABLE IF EXISTS `ubicacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ubicacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `departamento_id` bigint NOT NULL,
  `municipio_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ubicacion_departamento_id_be50b0a6_fk_departamentos_id` (`departamento_id`),
  KEY `ubicacion_municipio_id_09d5e5ab_fk_municipios_id` (`municipio_id`),
  CONSTRAINT `ubicacion_departamento_id_be50b0a6_fk_departamentos_id` FOREIGN KEY (`departamento_id`) REFERENCES `departamentos` (`id`),
  CONSTRAINT `ubicacion_municipio_id_09d5e5ab_fk_municipios_id` FOREIGN KEY (`municipio_id`) REFERENCES `municipios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubicacion`
--

LOCK TABLES `ubicacion` WRITE;
/*!40000 ALTER TABLE `ubicacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `ubicacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `password` varchar(128) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(15) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `tipo_usuario` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES ('pbkdf2_sha256$870000$NpKPTfivCCyO03WAX2ekk2$93T+f6nW5/jlR2HnhEdmgwUIk0b0E3rqC3wxu+Y+qNU=',1,'Admin','Conaldex Boyaca','rubendm965@gmail.com',1,1,1,'2024-10-17 18:06:04.834876','superuser'),('pbkdf2_sha256$870000$9KTxrIyZxAXpJ3r1PPo4Uo$yR8a50Ch86ECE4mg7N6YjNp91AaXqB1gW83u2mibVDA=',2,'Normal','Usuario Normal','Normal@hotmail.com',0,0,1,'2024-10-17 18:09:33.472014','usuario');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_groups`
--

DROP TABLE IF EXISTS `usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_groups_customuser_id_group_id_18e8ca87_uniq` (`customuser_id`,`group_id`),
  KEY `usuario_groups_group_id_c67c8651_fk_auth_group_id` (`group_id`),
  CONSTRAINT `usuario_groups_customuser_id_dae56c50_fk_usuario_id` FOREIGN KEY (`customuser_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `usuario_groups_group_id_c67c8651_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_groups`
--

LOCK TABLES `usuario_groups` WRITE;
/*!40000 ALTER TABLE `usuario_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_user_permissions`
--

DROP TABLE IF EXISTS `usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_user_permissions_customuser_id_permission_956f0d16_uniq` (`customuser_id`,`permission_id`),
  KEY `usuario_user_permiss_permission_id_a8893ce7_fk_auth_perm` (`permission_id`),
  CONSTRAINT `usuario_user_permiss_permission_id_a8893ce7_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `usuario_user_permissions_customuser_id_f3811ba0_fk_usuario_id` FOREIGN KEY (`customuser_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_user_permissions`
--

LOCK TABLES `usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuario_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `num_factura` varchar(10) NOT NULL,
  `fecha_emision` date NOT NULL,
  `cliente_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `num_factura` (`num_factura`),
  KEY `Venta_cliente_id_a2b0be2d_fk_Cliente_id` (`cliente_id`),
  CONSTRAINT `Venta_cliente_id_a2b0be2d_fk_Cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-17 13:30:52
