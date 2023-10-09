CREATE DATABASE  IF NOT EXISTS `chabella` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `chabella`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: chabella
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(90) DEFAULT NULL,
  `description` text,
  `id_category` int DEFAULT NULL,
  `image` text,
  `price` int DEFAULT NULL,
  `existence` int DEFAULT NULL,
  `likes` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_category` (`id_category`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`id_category`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (3,'TERERÉ TERMOLAR CUERO FUCSIA CON FAJA','Termo de terere con aplique',2,'https://media.aki.com.py/6387-large_default/terere-termolar-cuero-fucsia-con-faja.jpg',400000,0,0,5,'2023-03-05 20:37:32','2023-03-06 21:58:24'),(5,'MATERA TÉRMICA 236 ML','Disfruta tus aventuras con esta Matera Térmica 236 ml',1,'https://cdn.shopify.com/s/files/1/0216/0911/9808/products/Matera236_Negra_5000x.jpg?v=1663773295',90000,0,0,7,'2023-03-05 20:42:01','2023-03-05 20:42:01'),(6,'BOTELLA TÉRMICA 592ML','Disfruta tus aventuras al estilo con esta Botella Térmica 592ml',3,'https://cdn.shopify.com/s/files/1/0216/0911/9808/products/Botella-592ml-White-3_5000x.jpg?v=1663773315',90000,0,0,0,'2023-03-06 00:39:59','2023-03-06 00:39:59'),(7,'TERMO TAPA MAGNÉTICA 946ML','Disfruta tus aventuras  con este Termo Insulado 946ml',3,'https://cdn.shopify.com/s/files/1/0216/0911/9808/products/Termo-Magnet-White-4_5000x.jpg?v=1660847359',200000,0,0,0,'2023-03-06 00:44:50','2023-03-06 00:44:50'),(9,'TAZAS PERSONALIZADAS','Puedes conseguir tazas personalizadas baratas y totalmente a tu gusto.',4,'https://content-management-files.canva.com/cdn-cgi/image/f=auto,q=70/3ad1f2d5-1bb1-4df5-a414-dd9bbe8b7a96/header_MUGS2.jpg',30000,0,0,0,'2023-03-06 18:51:08','2023-03-06 18:51:08');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-07 14:10:12
