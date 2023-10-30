-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: av3
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `livro`
--

DROP TABLE IF EXISTS `livro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `livro` (
  `id` int NOT NULL,
  `versao` int NOT NULL DEFAULT '1',
  `nome` varchar(120) DEFAULT NULL,
  `genero` varchar(120) DEFAULT NULL,
  `autor` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`,`versao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livro`
--

LOCK TABLES `livro` WRITE;
/*!40000 ALTER TABLE `livro` DISABLE KEYS */;
INSERT INTO `livro` VALUES (1,4,'Harry Potter e a pedra filosoal','ficção','J. K. Howling'),(3,4,'O mundo asosmbrado pelos demônios','não-ficção','Carl Sagan'),(4,4,'As crônicas de gelo e fogo','ficção','R. R. Martin'),(5,4,'Sapiens: uma breve história da humanidade','não-ficção','Yuval Harari');
/*!40000 ALTER TABLE `livro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `livro_log`
--

DROP TABLE IF EXISTS `livro_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `livro_log` (
  `id` int NOT NULL,
  `versao` int NOT NULL,
  `nome` varchar(120) DEFAULT NULL,
  `genero` varchar(120) DEFAULT NULL,
  `autor` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`,`versao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livro_log`
--

LOCK TABLES `livro_log` WRITE;
/*!40000 ALTER TABLE `livro_log` DISABLE KEYS */;
INSERT INTO `livro_log` VALUES (1,1,'Harry Potter e a pedra filosoal','ficção','J. K. Howling'),(1,2,'Harry Potter e a pedraa filosoal','ficção','J. K. Howling'),(1,3,'Harry Potter e a pedraa filosoall','ficção','J. K. Howling'),(2,1,'O universo em uma casca de noz','não-ficção','Stephen Hawking'),(2,2,'O universo em uma cascaa de noz','não-ficção','Stephen Hawking'),(2,3,'O universo em uma cascaa de nozz','não-ficção','Stephen Hawking'),(2,4,'O universo em uma casca de noz','não-ficção','Stephen Hawking'),(2,5,'Uma breve história do tempo','não-ficção','Stephen King'),(2,6,'Uma breve história do tempo','não-ficção','Stephen Hawking'),(3,1,'O mundo asosmbrado pelos demônios','não-ficção','Carl Sagan'),(3,2,'O mundo asosmbrado peloss demônios','não-ficção','Carl Sagan'),(3,3,'O mundo asosmbrado peloss demônioss','não-ficção','Carl Sagan'),(4,1,'As crônicas de gelo e fogo','ficção','R. R. Martin'),(4,2,'As crônicas de gelo e fogoo','ficção','R. R. Martin'),(4,3,'As crônicas de gelo e fogoo','ficçãoo','R. R. Martin'),(5,1,'Sapiens: uma breve história da humanidade','não-ficção','Yuval Harari'),(5,2,'Sapiens: uma breve história da humanidadee','não-ficção','Yuval Harari'),(5,3,'Sapiens: uma breve história da humanidadeew','não-ficção','Yuval Harari');
/*!40000 ALTER TABLE `livro_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'av3'
--

--
-- Dumping routines for database 'av3'
--
/*!50003 DROP PROCEDURE IF EXISTS `Att_Livro` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Att_Livro`(
    IN n_id INT,
    IN n_nome VARCHAR(120),
    IN n_genero VARCHAR(120),
    IN n_autor VARCHAR(120)
)
BEGIN
    DECLARE versao_a INT;

    -- Encontra a versão atual do livro, se existir
    SELECT MAX(versao) INTO versao_a FROM livro WHERE id = n_id;

    -- Mover a versão atual para log
    IF versao_a IS NOT NULL THEN
        INSERT INTO livro_log (id, versao, nome, genero, autor)
        SELECT id, versao, nome, genero, autor
        FROM livro WHERE id = n_id;
    END IF;

    -- Atualizar o registro na tabela principal
    UPDATE livro
    SET nome = n_nome, genero = n_genero, autor = n_autor
    WHERE id = n_id;

    -- Incrementar a versão na tabela principal
    UPDATE livro
    SET versao = IFNULL(versao_a, 0) + 1
    WHERE id = n_id AND versao = versao_a;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `cadastro` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `cadastro`(
    IN n_id INT,
    IN n_nome VARCHAR(120),
    IN n_genero VARCHAR(120),
    IN n_autor VARCHAR(120)
)
BEGIN
    DECLARE versao_a INT;

    -- Encontra a versão atual do livro, se existir
    SELECT MAX(versao) INTO versao_a FROM livro WHERE id = n_id;

    -- Se o livro existe, move para livro_log
    IF versao_a IS NOT NULL THEN
        INSERT INTO livro_log (id, versao, nome, genero, autor)
        SELECT id, versao, nome, genero, autor
        FROM livro WHERE id = n_id;

	-- Remove todas as versões anteriores do livro na tabela principal
        DELETE FROM livro WHERE id = n_id;
    END IF;

    -- Insere o novo registro na tabela principal
    INSERT INTO livro (id, versao, nome, genero, autor)
    VALUES (n_id, IFNULL(versao_a, 0) + 1, n_nome, n_genero, n_autor);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `excluir` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `excluir`(
    IN n_id INT
)
BEGIN
    DECLARE versao_a INT;

    -- Encontra a versão atual do livro, se existir
    SELECT COALESCE(MAX(versao), 0) INTO versao_a FROM livro WHERE id = n_id;

    -- Mover o registro para livro_log antes de excluí-lo
    INSERT INTO livro_log (id, versao, nome, genero, autor)
    SELECT id, versao_a, nome, genero, autor
    FROM livro WHERE id = n_id AND versao = versao_a;

    -- Excluir o registro da tabela principal
    DELETE FROM livro WHERE id = n_id AND versao = versao_a;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-30 13:30:20
