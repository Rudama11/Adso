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
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
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
  `razon_social` varchar(150) DEFAULT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` varchar(10) DEFAULT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `direccion` varchar(50) DEFAULT NULL,
  `ciudad_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
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
  `num_factura` varchar(20) NOT NULL,
  `fecha_compra` datetime(6) NOT NULL,
  `proveedor_id` bigint NOT NULL,
  PRIMARY KEY (`num_factura`),
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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamentos`
--

LOCK TABLES `departamentos` WRITE;
/*!40000 ALTER TABLE `departamentos` DISABLE KEYS */;
INSERT INTO `departamentos` VALUES (1,'Amazonas'),(2,'Antioquia '),(3,'Arauca'),(4,'Atlántico '),(5,'Bolívar'),(6,'Boyacá'),(7,'Caldas'),(8,'Caquetá'),(9,'Casanare'),(10,'Cauca'),(11,'Cesar'),(12,'Chocó'),(13,'Córdoba'),(14,'Cundinamarca'),(15,'Guainía'),(16,'Guaviare'),(17,'Huila'),(18,'La Guajira'),(19,'Magdalena'),(20,'Meta'),(21,'Nariño'),(22,'Norte de Santander'),(23,'Putumayo'),(24,'Quindío'),(25,'Risaralda'),(26,'San Andrés y Providencia'),(27,'Santander'),(28,'Sucre'),(29,'Tolima'),(30,'Valle del Cauca'),(31,'Vaupés'),(32,'Vichada');
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
  `cantidad` int NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `iva` decimal(5,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `compra_id` varchar(20) NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DetalleCompra_compra_id_e9e73390_fk_Compras_num_factura` (`compra_id`),
  KEY `DetalleCompra_producto_id_8de69c74_fk_Producto_id` (`producto_id`),
  CONSTRAINT `DetalleCompra_compra_id_e9e73390_fk_Compras_num_factura` FOREIGN KEY (`compra_id`) REFERENCES `compras` (`num_factura`),
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
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-09-30 18:12:07.843713'),(2,'contenttypes','0002_remove_content_type_name','2024-09-30 18:12:07.888255'),(3,'auth','0001_initial','2024-09-30 18:12:08.081719'),(4,'auth','0002_alter_permission_name_max_length','2024-09-30 18:12:08.134893'),(5,'auth','0003_alter_user_email_max_length','2024-09-30 18:12:08.143400'),(6,'auth','0004_alter_user_username_opts','2024-09-30 18:12:08.147814'),(7,'auth','0005_alter_user_last_login_null','2024-09-30 18:12:08.155356'),(8,'auth','0006_require_contenttypes_0002','2024-09-30 18:12:08.157667'),(9,'auth','0007_alter_validators_add_error_messages','2024-09-30 18:12:08.161664'),(10,'auth','0008_alter_user_username_max_length','2024-09-30 18:12:08.166985'),(11,'auth','0009_alter_user_last_name_max_length','2024-09-30 18:12:08.170985'),(12,'auth','0010_alter_group_name_max_length','2024-09-30 18:12:08.179092'),(13,'auth','0011_update_proxy_permissions','2024-09-30 18:12:08.187445'),(14,'auth','0012_alter_user_first_name_max_length','2024-09-30 18:12:08.192602'),(15,'app','0001_initial','2024-09-30 18:12:09.417475'),(16,'admin','0001_initial','2024-09-30 18:12:09.553399'),(17,'admin','0002_logentry_remove_auto_add','2024-09-30 18:12:09.562397'),(18,'admin','0003_logentry_add_action_flag_choices','2024-09-30 18:12:09.571398'),(19,'inicio','0001_initial','2024-09-30 18:12:09.584398'),(20,'inicio','0002_delete_csrftoken','2024-09-30 18:12:09.608441'),(21,'sessions','0001_initial','2024-09-30 18:12:09.654648');
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
INSERT INTO `django_session` VALUES ('npzv66qwjnlsxy78rugyp5g2djjppv7e','.eJxVjMEOwiAQRP-FsyEslrJ49O43kIUFqRpISnsy_rtt0oPeJvPezFt4Wpfi155mP7G4CBCn3y5QfKa6A35QvTcZW13mKchdkQft8tY4va6H-3dQqJdtjTqfYRhDJk0W0xgsbWlwKrMiF7LGbFgTIyTGaABdBgtIDECsnBGfL_ljOF0:1svKxw:XySK5moUsKD2KokrQvqjYR9CLcqWMYXpw9zwHfYXaBE','2024-10-14 18:17:48.449358');
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
) ENGINE=InnoDB AUTO_INCREMENT=1124 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `municipios`
--

LOCK TABLES `municipios` WRITE;
/*!40000 ALTER TABLE `municipios` DISABLE KEYS */;
INSERT INTO `municipios` VALUES (1,'Abejorral ',2),(2,'Ábrego ',22),(3,'Abriaquí ',2),(4,'Acacías ',20),(5,'Acandí ',12),(6,'Acevedo ',17),(7,'Achí ',5),(8,'Agrado ',17),(9,'Agua De Dios ',14),(10,'Aguachica ',11),(11,'Aguada ',27),(12,'Aguadas ',7),(13,'Aguazul ',9),(14,'Agustín Codazzi ',11),(15,'Aipe ',17),(16,'Albán ',14),(17,'Albán (San José) ',21),(18,'Albania ',8),(19,'Albania ',18),(20,'Albania ',27),(21,'Alcalá ',30),(22,'Aldana ',21),(23,'Alejandría ',2),(24,'Algarrobo ',19),(25,'Algeciras ',17),(26,'Almaguer ',10),(27,'Almeida ',6),(28,'Alpujarra ',29),(29,'Altamira ',17),(30,'Alto Baudó (Pie De Pató) ',12),(31,'Altos Del Rosario ',5),(32,'Alvarado ',29),(33,'Amagá ',2),(34,'Amalfi ',2),(35,'Ambalema ',29),(36,'Anapoima ',14),(37,'Ancuyá ',21),(38,'Andalucía ',30),(39,'Andes ',2),(40,'Angelópolis ',2),(41,'Angostura ',2),(42,'Anolaima ',14),(43,'Anorí ',2),(44,'Anserma ',7),(45,'Ansermanuevo ',30),(46,'Anzá ',2),(47,'Anzoátegui ',29),(48,'Apartadó ',2),(49,'Apía ',25),(50,'Apulo ',14),(51,'Aquitania ',6),(52,'Aracataca ',19),(53,'Aranzazu ',7),(54,'Aratoca ',27),(55,'Arauca ',3),(56,'Arauquita ',3),(57,'Arbeláez ',14),(58,'Arboleda ',21),(59,'Arboledas ',22),(60,'Arboletes ',2),(61,'Arcabuco ',6),(62,'Arenal ',5),(63,'Argelia ',2),(64,'Argelia ',10),(65,'Argelia ',30),(66,'Ariguaní ',19),(67,'Arjona ',5),(68,'Armenia ',2),(69,'Armenia ',24),(70,'Armero (Guayabal) ',29),(71,'Arroyohondo ',5),(72,'Astrea ',11),(73,'Ataco ',29),(74,'Atrato (Yuto) ',12),(75,'Ayapel ',13),(76,'Bagadó ',12),(77,'Bahía Solano (Mutis) ',12),(78,'Bajo Baudó (Pizarro) ',12),(79,'Balboa ',10),(80,'Balboa ',25),(81,'Baranoa ',4),(82,'Baraya ',17),(83,'Barbacoas ',21),(84,'Barbosa ',2),(85,'Barbosa ',27),(86,'Barichara ',27),(87,'Barranca De Upía ',20),(88,'Barrancabermeja ',27),(89,'Barrancas ',18),(90,'Barranco De Loba ',5),(91,'Barrancominas ',15),(92,'Barranquilla ',4),(93,'Becerril ',11),(94,'Belalcázar ',7),(95,'Belén ',6),(96,'Belén ',21),(97,'Belén De Los Andaquíes ',8),(98,'Belén De Umbría ',25),(99,'Bello ',2),(100,'Belmira ',2),(101,'Beltrán ',14),(102,'Berbeo ',6),(103,'Betania ',2),(104,'Betéitiva ',6),(105,'Betulia ',2),(106,'Betulia ',27),(107,'Bituima ',14),(108,'Boavita ',6),(109,'Bochalema ',22),(110,'Bogotá D.C. ',14),(111,'Bojacá ',14),(112,'Bojayá (Bella Vista) ',12),(113,'Bolívar ',10),(114,'Bolívar ',27),(115,'Bolívar ',30),(116,'Bosconia ',11),(117,'Boyacá ',6),(118,'Briceño ',2),(119,'Briceño ',6),(120,'Bucaramanga ',27),(121,'Bucarasica ',22),(122,'Buenaventura ',30),(123,'Buenavista ',6),(124,'Buenavista ',13),(125,'Buenavista ',24),(126,'Buenavista ',28),(127,'Buenos Aires ',10),(128,'Buesaco ',21),(129,'Bugalagrande ',30),(130,'Buriticá ',2),(131,'Busbanzá ',6),(132,'Cabrera ',14),(133,'Cabrera ',27),(134,'Cabuyaro ',20),(135,'Cacahual ',15),(136,'Cáceres ',2),(137,'Cachipay ',14),(138,'Cáchira ',22),(139,'Cácota De Velasco ',22),(140,'Caicedo ',2),(141,'Caicedonia ',30),(142,'Caimito ',28),(143,'Cajamarca ',29),(144,'Cajibío ',10),(145,'Cajicá ',14),(146,'Calamar ',5),(147,'Calamar ',16),(148,'Calarcá ',24),(149,'Caldas ',2),(150,'Caldas ',6),(151,'Caldono ',10),(152,'Cali ',30),(153,'California ',27),(154,'Calima (Darien) ',30),(155,'Caloto ',10),(156,'Campamento ',2),(157,'Campo De La Cruz ',4),(158,'Campoalegre ',17),(159,'Campohermoso ',6),(160,'Canalete ',13),(161,'Candelaria ',4),(162,'Candelaria ',30),(163,'Cantagallo ',5),(164,'Cañasgordas ',2),(165,'Caparrapí ',14),(166,'Capitanejo ',27),(167,'Cáqueza ',14),(168,'Caracolí ',2),(169,'Caramanta ',2),(170,'Carcasí ',27),(171,'Carepa ',2),(172,'Carmen De Apicalá ',29),(173,'Carmen De Carupa ',14),(174,'Carmen Del Darién ',12),(175,'Carolina ',2),(176,'Cartagena De Indias ',5),(177,'Cartagena Del Chairá ',8),(178,'Cartago ',30),(179,'Carurú ',31),(180,'Casabianca ',29),(181,'Castilla La Nueva ',20),(182,'Caucasia ',2),(183,'Cepitá ',27),(184,'Cereté ',13),(185,'Cerinza ',6),(186,'Cerrito ',27),(187,'Cerro De San Antonio ',19),(188,'Cértegui ',12),(189,'Chachagüí ',21),(190,'Chaguaní ',14),(191,'Chalán ',28),(192,'Chámeza ',9),(193,'Chaparral ',29),(194,'Charalá ',27),(195,'Charta ',27),(196,'Chía ',14),(197,'Chibolo ',19),(198,'Chigorodó ',2),(199,'Chima ',27),(200,'Chimá ',13),(201,'Chimichagua ',11),(202,'Chinácota ',22),(203,'Chinavita ',6),(204,'Chinchiná ',7),(205,'Chinú ',13),(206,'Chipaque ',14),(207,'Chipatá ',27),(208,'Chiquinquirá ',6),(209,'Chíquiza ',6),(210,'Chiriguaná ',11),(211,'Chiscas ',6),(212,'Chita ',6),(213,'Chitagá ',22),(214,'Chitaraque ',6),(215,'Chivatá ',6),(216,'Chivor ',6),(217,'Choachí ',14),(218,'Chocontá ',14),(219,'Cicuco ',5),(220,'Ciénaga ',19),(221,'Ciénaga De Oro ',13),(222,'Ciénega ',6),(223,'Cimitarra ',27),(224,'Circasia ',24),(225,'Cisneros ',2),(226,'Ciudad Bolívar ',2),(227,'Clemencia ',5),(228,'Cocorná ',2),(229,'Coello ',29),(230,'Cogua ',14),(231,'Colombia ',17),(232,'Colón ',23),(233,'Colón (Génova) ',21),(234,'Colosó ',28),(235,'Cómbita ',6),(236,'Concepción ',2),(237,'Concepción ',27),(238,'Concordia ',2),(239,'Concordia ',19),(240,'Condoto ',12),(241,'Confines ',27),(242,'Consacá ',21),(243,'Contadero ',21),(244,'Contratación ',27),(245,'Convención ',22),(246,'Copacabana ',2),(247,'Coper ',6),(248,'Córdoba ',5),(249,'Córdoba ',21),(250,'Córdoba ',24),(251,'Corinto ',10),(252,'Coromoro ',27),(253,'Corozal ',28),(254,'Corrales ',6),(255,'Cota ',14),(256,'Cotorra ',13),(257,'Covarachía ',6),(258,'Coveñas ',28),(259,'Coyaima ',29),(260,'Cravo Norte ',3),(261,'Cuaspúd ',21),(262,'Cubará ',6),(263,'Cubarral ',20),(264,'Cucaita ',6),(265,'Cucunubá ',14),(266,'Cúcuta ',22),(267,'Cucutilla ',22),(268,'Cuítiva ',6),(269,'Cumaral ',20),(270,'Cumaribo ',32),(271,'Cumbal ',21),(272,'Cumbitara ',21),(273,'Cunday ',29),(274,'Curillo ',8),(275,'Curití ',27),(276,'Curumaní ',11),(277,'Dabeiba ',2),(278,'Dagua ',30),(279,'Dibulla ',18),(280,'Distracción ',18),(281,'Dolores ',29),(282,'Donmatías ',2),(283,'Dosquebradas ',25),(284,'Duitama ',6),(285,'Durania ',22),(286,'Ebéjico ',2),(287,'El Águila ',30),(288,'El Bagre ',2),(289,'El Banco ',19),(290,'El Cairo ',30),(291,'El Calvario ',20),(292,'El Cantón Del San Pablo ',12),(293,'El Carmen ',22),(294,'El Carmen De Atrato ',12),(295,'El Carmen De Bolívar ',5),(296,'El Carmen De Chucurí ',27),(297,'El Carmen De Viboral ',2),(298,'El Castillo ',20),(299,'El Cerrito ',30),(300,'El Charco ',21),(301,'El Cocuy ',6),(302,'El Colegio ',14),(303,'El Copey ',11),(304,'El Doncello ',8),(305,'El Dorado ',20),(306,'El Dovio ',30),(307,'El Encanto ',1),(308,'El Espino ',6),(309,'El Guacamayo ',27),(310,'El Guamo ',5),(311,'El Litoral Del San Juan ',12),(312,'El Molino ',18),(313,'El Paso ',11),(314,'El Paujíl ',8),(315,'El Peñol ',21),(316,'El Peñón ',5),(317,'El Peñón ',14),(318,'El Peñón ',27),(319,'El Piñón ',19),(320,'El Playón ',27),(321,'El Retén ',19),(322,'El Retorno ',16),(323,'El Roble ',28),(324,'El Rosal ',14),(325,'El Rosario ',21),(326,'El Santuario ',2),(327,'El Tablón De Gómez ',21),(328,'El Tambo ',10),(329,'El Tambo ',21),(330,'El Tarra ',22),(331,'El Zulia ',22),(332,'Elías ',17),(333,'Encino ',27),(334,'Enciso ',27),(335,'Entrerríos ',2),(336,'Envigado ',2),(337,'Espinal ',29),(338,'Facatativá ',14),(339,'Falan ',29),(340,'Filadelfia ',7),(341,'Filandia ',24),(342,'Firavitoba ',6),(343,'Flandes ',29),(344,'Florencia ',8),(345,'Florencia ',10),(346,'Floresta ',6),(347,'Florián ',27),(348,'Florida ',30),(349,'Floridablanca ',27),(350,'Fómeque ',14),(351,'Fonseca ',18),(352,'Fortul ',3),(353,'Fosca ',14),(354,'Francisco Pizarro ',21),(355,'Fredonia ',2),(356,'Fresno ',29),(357,'Frontino ',2),(358,'Fuentedeoro ',20),(359,'Fundación ',19),(360,'Funes ',21),(361,'Funza ',14),(362,'Fúquene ',14),(363,'Fusagasugá ',14),(364,'Gachalá ',14),(365,'Gachancipá ',14),(366,'Gachantivá ',6),(367,'Gachetá ',14),(368,'Galán ',27),(369,'Galapa ',4),(370,'Galeras ',28),(371,'Gama ',14),(372,'Gamarra ',11),(373,'Gámbita ',27),(374,'Gámeza ',6),(375,'Garagoa ',6),(376,'Garzón ',17),(377,'Génova ',24),(378,'Gigante ',17),(379,'Ginebra ',30),(380,'Giraldo ',2),(381,'Girardot ',14),(382,'Girardota ',2),(383,'Girón ',27),(384,'Gómez Plata ',2),(385,'González ',11),(386,'Gramalote ',22),(387,'Granada ',2),(388,'Granada ',14),(389,'Granada ',20),(390,'Guaca ',27),(391,'Guacamayas ',6),(392,'Guacarí ',30),(393,'Guachené ',10),(394,'Guachetá ',14),(395,'Guachucal ',21),(396,'Guadalajara De Buga ',30),(397,'Guadalupe ',2),(398,'Guadalupe ',17),(399,'Guadalupe ',27),(400,'Guaduas ',14),(401,'Guaitarilla ',21),(402,'Gualmatán ',21),(403,'Guamal ',19),(404,'Guamal ',20),(405,'Guamo ',29),(406,'Guapí ',10),(407,'Guapotá ',27),(408,'Guaranda ',28),(409,'Guarne ',2),(410,'Guasca ',14),(411,'Guatapé ',2),(412,'Guataquí ',14),(413,'Guatavita ',14),(414,'Guateque ',6),(415,'Guática ',25),(416,'Guavatá ',27),(417,'Guayabal De Síquima ',14),(418,'Guayabetal ',14),(419,'Guayatá ',6),(420,'Güepsa ',27),(421,'Güicán De La Sierra ',6),(422,'Gutiérrez ',14),(423,'Hacarí ',22),(424,'Hatillo De Loba ',5),(425,'Hato ',27),(426,'Hato Corozal ',9),(427,'Hatonuevo ',18),(428,'Heliconia ',2),(429,'Herrán ',22),(430,'Herveo ',29),(431,'Hispania ',2),(432,'Hobo ',17),(433,'Honda ',29),(434,'Ibagué ',29),(435,'Icononzo ',29),(436,'Iles ',21),(437,'Imués ',21),(438,'Inírida ',15),(439,'Inzá ',10),(440,'Ipiales ',21),(441,'Íquira ',17),(442,'Isnos ',17),(443,'Istmina ',12),(444,'Itagüí ',2),(445,'Ituango ',2),(446,'Iza ',6),(447,'Jambaló ',10),(448,'Jamundí ',30),(449,'Jardín ',2),(450,'Jenesano ',6),(451,'Jericó ',2),(452,'Jericó ',6),(453,'Jerusalén ',14),(454,'Jesús María ',27),(455,'Jordán ',27),(456,'Juan De Acosta ',4),(457,'Junín ',14),(458,'Juradó ',12),(459,'La Apartada ',13),(460,'La Argentina (La Plata Vieja) ',17),(461,'La Belleza ',27),(462,'La Calera ',14),(463,'La Capilla ',6),(464,'La Ceja ',2),(465,'La Celia ',25),(466,'La Chorrera ',1),(467,'La Cruz ',21),(468,'La Cumbre ',30),(469,'La Dorada ',7),(470,'La Esperanza ',22),(471,'La Estrella ',2),(472,'La Florida ',21),(473,'La Gloria ',11),(474,'La Guadalupe ',15),(475,'La Jagua De Ibirico ',11),(476,'La Jagua Del Pilar ',18),(477,'La Llanada ',21),(478,'La Macarena ',20),(479,'La Merced ',7),(480,'La Mesa ',14),(481,'La Montañita ',8),(482,'La Palma ',14),(483,'La Paz ',11),(484,'La Paz ',27),(485,'La Pedrera ',1),(486,'La Peña ',14),(487,'La Pintada ',2),(488,'La Plata ',17),(489,'La Playa De Belén ',22),(490,'La Primavera ',32),(491,'La Salina ',9),(492,'La Sierra ',10),(493,'La Tebaida ',24),(494,'La Tola ',21),(495,'La Unión ',2),(496,'La Unión ',21),(497,'La Unión ',28),(498,'La Unión ',30),(499,'La Uvita ',6),(500,'La Vega ',10),(501,'La Vega ',14),(502,'La Victoria ',1),(503,'La Victoria ',6),(504,'La Victoria ',30),(505,'La Virginia ',25),(506,'Labateca ',22),(507,'Labranzagrande ',6),(508,'Landázuri ',27),(509,'Lebrija ',27),(510,'Leiva ',21),(511,'Lejanías ',20),(512,'Lenguazaque ',14),(513,'Lérida ',29),(514,'Leticia ',1),(515,'Líbano ',29),(516,'Liborina ',2),(517,'Linares ',21),(518,'Lloró ',12),(519,'López De Micay ',10),(520,'Lorica ',13),(521,'Los Andes (Sotomayor) ',21),(522,'Los Córdobas ',13),(523,'Los Palmitos ',28),(524,'Los Patios ',22),(525,'Los Santos ',27),(526,'Lourdes ',22),(527,'Luruaco ',4),(528,'Macanal ',6),(529,'Macaravita ',27),(530,'Maceo ',2),(531,'Machetá ',14),(532,'Madrid ',14),(533,'Magangué ',5),(534,'Magüí (Payán) ',21),(535,'Mahates ',5),(536,'Maicao ',18),(537,'Majagual ',28),(538,'Málaga ',27),(539,'Malambo ',4),(540,'Mallama (Piedrancha) ',21),(541,'Manatí ',4),(542,'Manaure ',18),(543,'Manaure Balcón Del Cesar ',11),(544,'Maní ',9),(545,'Manizales ',7),(546,'Manta ',14),(547,'Manzanares ',7),(548,'Mapiripán ',20),(549,'Mapiripana ',15),(550,'Margarita ',5),(551,'María La Baja ',5),(552,'Marinilla ',2),(553,'Maripí ',6),(554,'Marmato ',7),(555,'Marquetalia ',7),(556,'Marsella ',25),(557,'Marulanda ',7),(558,'Matanza ',27),(559,'Medellín ',2),(560,'Medina ',14),(561,'Medio Atrato (Beté) ',12),(562,'Medio Baudó ',12),(563,'Medio San Juan (Andagoya) ',12),(564,'Melgar ',29),(565,'Mercaderes ',10),(566,'Mesetas ',20),(567,'Milán ',8),(568,'Miraflores ',6),(569,'Miraflores ',16),(570,'Miranda ',10),(571,'Mirití – Paraná ',1),(572,'Mistrató ',25),(573,'Mitú ',31),(574,'Mocoa ',23),(575,'Mogotes ',27),(576,'Molagavita ',27),(577,'Momil ',13),(578,'Mompós ',5),(579,'Mongua ',6),(580,'Monguí ',6),(581,'Moniquirá ',6),(582,'Montebello ',2),(583,'Montecristo ',5),(584,'Montelíbano ',13),(585,'Montenegro ',24),(586,'Montería ',13),(587,'Monterrey ',9),(588,'Moñitos ',13),(589,'Morales ',5),(590,'Morales ',10),(591,'Morelia ',8),(592,'Morichal Nuevo ',15),(593,'Morroa ',28),(594,'Mosquera ',14),(595,'Mosquera ',21),(596,'Motavita ',6),(597,'Murillo ',29),(598,'Murindó ',2),(599,'Mutatá ',2),(600,'Mutiscua ',22),(601,'Muzo ',6),(602,'Nariño ',2),(603,'Nariño ',14),(604,'Nariño ',21),(605,'Nátaga ',17),(606,'Natagaima ',29),(607,'Nechí ',2),(608,'Necoclí ',2),(609,'Neira ',7),(610,'Neiva ',17),(611,'Nemocón ',14),(612,'Nilo ',14),(613,'Nimaima ',14),(614,'Nobsa ',6),(615,'Nocaima ',14),(616,'Norcasia ',7),(617,'Norosí ',5),(618,'Nóvita ',12),(619,'Nueva Granada ',19),(620,'Nuevo Colón ',6),(621,'Nunchía ',9),(622,'Nuquí ',12),(623,'Obando ',30),(624,'Ocamonte ',27),(625,'Ocaña ',22),(626,'Oiba ',27),(627,'Oicatá ',6),(628,'Olaya ',2),(629,'Olaya Herrera ',21),(630,'Onzaga ',27),(631,'Oporapa ',17),(632,'Orito ',23),(633,'Orocué ',9),(634,'Ortega ',29),(635,'Ospina ',21),(636,'Otanche ',6),(637,'Ovejas ',28),(638,'Pachavita ',6),(639,'Pacho ',14),(640,'Pacoa ',31),(641,'Pácora ',7),(642,'Padilla ',10),(643,'Páez ',6),(644,'Páez - Belalcazar ',10),(645,'Paicol ',17),(646,'Pailitas ',11),(647,'Paime ',14),(648,'Paipa ',6),(649,'Pajarito ',6),(650,'Palermo ',17),(651,'Palestina ',7),(652,'Palestina ',17),(653,'Palmar ',27),(654,'Palmar De Varela ',4),(655,'Palmas Del Socorro ',27),(656,'Palmira ',30),(657,'Palmito ',28),(658,'Palocabildo ',29),(659,'Pamplona ',22),(660,'Pamplonita ',22),(661,'Pana Pana ',15),(662,'Pandi ',14),(663,'Panqueba ',6),(664,'Papunahua ',31),(665,'Páramo ',27),(666,'Paratebueno ',14),(667,'Pasca ',14),(668,'Pasto ',21),(669,'Patía – El Bordo ',10),(670,'Pauna ',6),(671,'Paya ',6),(672,'Paz De Ariporo ',9),(673,'Paz De Río ',6),(674,'Pedraza ',19),(675,'Pelaya ',11),(676,'Pensilvania ',7),(677,'Peñol ',2),(678,'Peque ',2),(679,'Pereira ',25),(680,'Pesca ',6),(681,'Piamonte ',10),(682,'Piedecuesta ',27),(683,'Piedras ',29),(684,'Piendamó – Tunía ',10),(685,'Pijao ',24),(686,'Pijiño Del Carmen ',19),(687,'Pinchote ',27),(688,'Pinillos ',5),(689,'Piojó ',4),(690,'Pisba ',6),(691,'Pital ',17),(692,'Pitalito ',17),(693,'Pivijay ',19),(694,'Planadas ',29),(695,'Planeta Rica ',13),(696,'Plato ',19),(697,'Policarpa ',21),(698,'Polonuevo ',4),(699,'Ponedera ',4),(700,'Popayán ',10),(701,'Pore ',9),(702,'Potosí ',21),(703,'Pradera ',30),(704,'Prado ',29),(705,'Providencia ',26),(706,'Providencia ',21),(707,'Pueblo Bello ',11),(708,'Pueblo Nuevo ',13),(709,'Pueblo Rico ',25),(710,'Pueblorrico ',2),(711,'Puebloviejo ',19),(712,'Puente Nacional ',27),(713,'Puerres ',21),(714,'Puerto Alegría ',1),(715,'Puerto Arica ',1),(716,'Puerto Asís ',23),(717,'Puerto Berrío ',2),(718,'Puerto Boyacá ',6),(719,'Puerto Caicedo ',23),(720,'Puerto Carreño ',32),(721,'Puerto Colombia ',4),(722,'Puerto Colombia ',15),(723,'Puerto Concordia ',20),(724,'Puerto Escondido ',13),(725,'Puerto Gaitán ',20),(726,'Puerto Guzmán ',23),(727,'Puerto Leguízamo ',23),(728,'Puerto Libertador ',13),(729,'Puerto Lleras ',20),(730,'Puerto López ',20),(731,'Puerto Nare ',2),(732,'Puerto Nariño ',1),(733,'Puerto Parra ',27),(734,'Puerto Rico ',8),(735,'Puerto Rico ',20),(736,'Puerto Rondón ',3),(737,'Puerto Salgar ',14),(738,'Puerto Santander ',1),(739,'Puerto Santander ',22),(740,'Puerto Tejada ',10),(741,'Puerto Triunfo ',2),(742,'Puerto Wilches ',27),(743,'Pulí ',14),(744,'Pupiales ',21),(745,'Puracé - Coconuco ',10),(746,'Purificación ',29),(747,'Purísima De La Concepción ',13),(748,'Quebradanegra ',14),(749,'Quetame ',14),(750,'Quibdó ',12),(751,'Quimbaya ',24),(752,'Quinchía ',25),(753,'Quípama ',6),(754,'Quipile ',14),(755,'Ragonvalia ',22),(756,'Ramiriquí ',6),(757,'Ráquira ',6),(758,'Recetor ',9),(759,'Regidor ',5),(760,'Remedios ',2),(761,'Remolino ',19),(762,'Repelón ',4),(763,'Restrepo ',20),(764,'Restrepo ',30),(765,'Retiro ',2),(766,'Ricaurte ',14),(767,'Ricaurte ',21),(768,'Río De Oro ',11),(769,'Río Iró (Santa Rita) ',12),(770,'Río Quito (Paimadó) ',12),(771,'Río Viejo ',5),(772,'Rioblanco ',29),(773,'Riofrío ',30),(774,'Riohacha ',18),(775,'Rionegro ',2),(776,'Rionegro ',27),(777,'Riosucio ',7),(778,'Riosucio ',12),(779,'Risaralda ',7),(780,'Rivera ',17),(781,'Roberto Payán (San José) ',21),(782,'Roldanillo ',30),(783,'Roncesvalles ',29),(784,'Rondón ',6),(785,'Rosas ',10),(786,'Rovira ',29),(787,'Sabana De Torres ',27),(788,'Sabanagrande ',4),(789,'Sabanalarga ',2),(790,'Sabanalarga ',4),(791,'Sabanalarga ',9),(792,'Sabanas De San Ángel ',19),(793,'Sabaneta ',2),(794,'Saboyá ',6),(795,'Sácama ',9),(796,'Sáchica ',6),(797,'Sahagún ',13),(798,'Saladoblanco ',17),(799,'Salamina ',7),(800,'Salamina ',19),(801,'Salazar De Las Palmas ',22),(802,'Saldaña ',29),(803,'Salento ',24),(804,'Salgar ',2),(805,'Samacá ',6),(806,'Samaná ',7),(807,'Samaniego ',21),(808,'Sampués ',28),(809,'San Agustín ',17),(810,'San Alberto ',11),(811,'San Andrés ',26),(812,'San Andrés ',27),(813,'San Andrés De Cuerquía ',2),(814,'San Andrés De Sotavento ',13),(815,'San Andrés De Tumaco ',21),(816,'San Antero ',13),(817,'San Antonio ',29),(818,'San Antonio Del Tequendama ',14),(819,'San Benito ',27),(820,'San Benito Abad ',28),(821,'San Bernardo ',14),(822,'San Bernardo ',21),(823,'San Bernardo Del Viento ',13),(824,'San Calixto ',22),(825,'San Carlos ',2),(826,'San Carlos ',13),(827,'San Carlos De Guaroa ',20),(828,'San Cayetano ',14),(829,'San Cayetano ',22),(830,'San Cristóbal ',5),(831,'San Diego ',11),(832,'San Eduardo ',6),(833,'San Estanislao ',5),(834,'San Felipe ',15),(835,'San Fernando ',5),(836,'San Francisco ',2),(837,'San Francisco ',14),(838,'San Francisco ',23),(839,'San Gil ',27),(840,'San Jacinto ',5),(841,'San Jacinto Del Cauca ',5),(842,'San Jerónimo ',2),(843,'San Joaquín ',27),(844,'San José ',7),(845,'San José De La Montaña ',2),(846,'San José De Miranda ',27),(847,'San José De Pare ',6),(848,'San José De Uré ',13),(849,'San José Del Fragua ',8),(850,'San José Del Guaviare ',16),(851,'San José Del Palmar ',12),(852,'San Juan De Arama ',20),(853,'San Juan De Betulia ',28),(854,'San Juan De Rioseco ',14),(855,'San Juan De Urabá ',2),(856,'San Juan Del Cesar ',18),(857,'San Juan Nepomuceno ',5),(858,'San Juanito ',20),(859,'San Lorenzo ',21),(860,'San Luis ',2),(861,'San Luis ',29),(862,'San Luis De Gaceno ',6),(863,'San Luis De Palenque ',9),(864,'San Luis De Sincé ',28),(865,'San Marcos ',28),(866,'San Martín ',11),(867,'San Martín De Loba ',5),(868,'San Martín De Los Llanos ',20),(869,'San Mateo ',6),(870,'San Miguel ',23),(871,'San Miguel ',27),(872,'San Miguel De Sema ',6),(873,'San Onofre ',28),(874,'San Pablo ',21),(875,'San Pablo De Borbur ',6),(876,'San Pablo Sur ',5),(877,'San Pedro ',28),(878,'San Pedro ',30),(879,'San Pedro De Cartago ',21),(880,'San Pedro De Los Milagros ',2),(881,'San Pedro De Urabá ',2),(882,'San Pelayo ',13),(883,'San Rafael ',2),(884,'San Roque ',2),(885,'San Sebastián ',10),(886,'San Sebastián De Buenavista ',19),(887,'San Sebastián De Mariquita ',29),(888,'San Vicente De Chucurí ',27),(889,'San Vicente Del Caguán ',8),(890,'San Vicente Ferrer ',2),(891,'San Zenón ',19),(892,'Sandoná ',21),(893,'Santa Ana ',19),(894,'Santa Bárbara ',2),(895,'Santa Bárbara ',21),(896,'Santa Bárbara ',27),(897,'Santa Bárbara De Pinto ',19),(898,'Santa Catalina ',5),(899,'Santa Fé De Antioquia ',2),(900,'Santa Helena Del Opón ',27),(901,'Santa Isabel ',29),(902,'Santa Lucía ',4),(903,'Santa María ',6),(904,'Santa María ',17),(905,'Santa Marta ',19),(906,'Santa Rosa ',10),(907,'Santa Rosa De Cabal ',25),(908,'Santa Rosa De Lima ',5),(909,'Santa Rosa De Osos ',2),(910,'Santa Rosa De Viterbo ',6),(911,'Santa Rosa Del Sur ',5),(912,'Santa Rosalía ',32),(913,'Santa Sofía ',6),(914,'Santacruz ',21),(915,'Santana ',6),(916,'Santander De Quilichao ',10),(917,'Santiago ',22),(918,'Santiago ',23),(919,'Santiago De Tolú ',28),(920,'Santo Domingo ',2),(921,'Santo Domingo De Silos ',22),(922,'Santo Tomás ',4),(923,'Santuario ',25),(924,'Sapuyes ',21),(925,'Saravena ',3),(926,'Sardinata ',22),(927,'Sasaima ',14),(928,'Sativanorte ',6),(929,'Sativasur ',6),(930,'Segovia ',2),(931,'Sesquilé ',14),(932,'Sevilla ',30),(933,'Siachoque ',6),(934,'Sibaté ',14),(935,'Sibundoy ',23),(936,'Silvania ',14),(937,'Silvia ',10),(938,'Simacota ',27),(939,'Simijaca ',14),(940,'Simití ',5),(941,'Sincelejo ',28),(942,'Sipí ',12),(943,'Sitionuevo ',19),(944,'Soacha ',14),(945,'Soatá ',6),(946,'Socha ',6),(947,'Socorro ',27),(948,'Socotá ',6),(949,'Sogamoso ',6),(950,'Solano ',8),(951,'Soledad ',4),(952,'Solita ',8),(953,'Somondoco ',6),(954,'Sonsón ',2),(955,'Sopetrán ',2),(956,'Soplaviento ',5),(957,'Sopó ',14),(958,'Sora ',6),(959,'Soracá ',6),(960,'Sotaquirá ',6),(961,'Sotara ',10),(962,'Suaita ',27),(963,'Suan ',4),(964,'Suárez ',10),(965,'Suárez ',29),(966,'Suaza ',17),(967,'Subachoque ',14),(968,'Sucre ',10),(969,'Sucre ',27),(970,'Sucre ',28),(971,'Suesca ',14),(972,'Supatá ',14),(973,'Supía ',7),(974,'Suratá ',27),(975,'Susa ',14),(976,'Susacón ',6),(977,'Sutamarchán ',6),(978,'Sutatausa ',14),(979,'Sutatenza ',6),(980,'Tabio ',14),(981,'Tadó ',12),(982,'Talaigua Nuevo ',5),(983,'Tamalameque ',11),(984,'Támara ',9),(985,'Tame ',3),(986,'Támesis ',2),(987,'Taminango ',21),(988,'Tangua ',21),(989,'Taraira ',31),(990,'Tarapacá ',1),(991,'Tarazá ',2),(992,'Tarqui ',17),(993,'Tarso ',2),(994,'Tasco ',6),(995,'Tauramena ',9),(996,'Tausa ',14),(997,'Tello ',17),(998,'Tena ',14),(999,'Tenerife ',19),(1000,'Tenjo ',14),(1001,'Tenza ',6),(1002,'Teorama ',22),(1003,'Teruel ',17),(1004,'Tesalia (Carnicerías) ',17),(1005,'Tibacuy ',14),(1006,'Tibaná ',6),(1007,'Tibasosa ',6),(1008,'Tibirita ',14),(1009,'Tibú ',22),(1010,'Tierralta ',13),(1011,'Timaná ',17),(1012,'Timbío ',10),(1013,'Timbiquí ',10),(1014,'Tinjacá ',6),(1015,'Tipacoque ',6),(1016,'Tiquisio ',5),(1017,'Titiribí ',2),(1018,'Toca ',6),(1019,'Tocaima ',14),(1020,'Tocancipá ',14),(1021,'Togüí ',6),(1022,'Toledo ',2),(1023,'Toledo ',22),(1024,'Tolú Viejo ',28),(1025,'Tona ',27),(1026,'Tópaga ',6),(1027,'Topaipí ',14),(1028,'Toribío ',10),(1029,'Toro ',30),(1030,'Tota ',6),(1031,'Totoró ',10),(1032,'Trinidad ',9),(1033,'Trujillo ',30),(1034,'Tubará ',4),(1035,'Tuchín ',13),(1036,'Tuluá ',30),(1037,'Tunja ',6),(1038,'Tununguá ',6),(1039,'Túquerres ',21),(1040,'Turbaco ',5),(1041,'Turbaná ',5),(1042,'Turbo ',2),(1043,'Turmequé ',6),(1044,'Tuta ',6),(1045,'Tutazá ',6),(1046,'Ubalá ',14),(1047,'Ubaque ',14),(1048,'Ulloa ',30),(1049,'Úmbita ',6),(1050,'Une ',14),(1051,'Unguía ',12),(1052,'Unión Panamericana (Las Ánimas) ',12),(1053,'Uramita ',2),(1054,'Uribe ',20),(1055,'Uribia ',18),(1056,'Urrao ',2),(1057,'Urumita ',18),(1058,'Usiacurí ',4),(1059,'Útica ',14),(1060,'Valdivia ',2),(1061,'Valencia ',13),(1062,'Valle De San José ',27),(1063,'Valle De San Juan ',29),(1064,'Valle Del Guamuez ',23),(1065,'Valledupar ',11),(1066,'Valparaíso ',2),(1067,'Valparaíso ',8),(1068,'Vegachí ',2),(1069,'Vélez ',27),(1070,'Venadillo ',29),(1071,'Venecia ',2),(1072,'Venecia ',2),(1073,'Venecia ',14),(1074,'Ventaquemada ',6),(1075,'Vergara ',14),(1076,'Versalles ',30),(1077,'Vetas ',27),(1078,'Vianí ',14),(1079,'Victoria ',7),(1080,'Vigía Del Fuerte ',2),(1081,'Vijes ',30),(1082,'Villa Caro ',22),(1083,'Villa De Leyva ',6),(1084,'Villa De San Diego De Ubaté ',14),(1085,'Villa Del Rosario ',22),(1086,'Villa Rica ',10),(1087,'Villagarzón ',23),(1088,'Villagómez ',14),(1089,'Villahermosa ',29),(1090,'Villamaría ',7),(1091,'Villanueva ',5),(1092,'Villanueva ',9),(1093,'Villanueva ',18),(1094,'Villanueva ',27),(1095,'Villapinzón ',14),(1096,'Villarrica ',29),(1097,'Villavicencio ',20),(1098,'Villavieja ',17),(1099,'Villeta ',14),(1100,'Viotá ',14),(1101,'Viracachá ',6),(1102,'Vistahermosa ',20),(1103,'Viterbo ',7),(1104,'Yacopí ',14),(1105,'Yacuanquer ',21),(1106,'Yaguará ',17),(1107,'Yalí ',2),(1108,'Yarumal ',2),(1109,'Yavaraté ',31),(1110,'Yolombó ',2),(1111,'Yondó ',2),(1112,'Yopal ',9),(1113,'Yotoco ',30),(1114,'Yumbo ',30),(1115,'Zambrano ',5),(1116,'Zapatoca ',27),(1117,'Zapayán ',19),(1118,'Zaragoza ',2),(1119,'Zarzal ',30),(1120,'Zetaquira ',6),(1121,'Zipacón ',14),(1122,'Zipaquirá ',14),(1123,'Zona Bananera ',19);
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
  `decreto` varchar(25) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
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
  `nombre` varchar(150) NOT NULL,
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
  `razon_social` varchar(150) DEFAULT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` varchar(10) DEFAULT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `direccion` varchar(50) DEFAULT NULL,
  `ciudad_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
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
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo`
--

LOCK TABLES `tipo` WRITE;
/*!40000 ALTER TABLE `tipo` DISABLE KEYS */;
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
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(150) NOT NULL,
  `nombres` varchar(30) NOT NULL,
  `password` varchar(128) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `tipo_usuario` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Admin','','pbkdf2_sha256$870000$DvahmfX1EC441sYNSWflCv$O848VB60wjQJHDSOq0HM8u3uLERY6aeB/50O3fl3pPQ=','conaldex@gmail.com',1,1,1,'2024-09-30 18:17:48.449358','admin');
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
  `fecha_emision` datetime(6) NOT NULL,
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

-- Dump completed on 2024-09-30 13:18:12
