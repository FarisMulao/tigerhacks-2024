DROP DATABASE IF EXISTS pliddb;

CREATE DATABASE pliddb /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

DROP USER IF EXISTS plidbackend@localhost;

CREATE USER plidbackend@localhost IDENTIFIED BY 'password';

USE pliddb;

GRANT DELETE, EXECUTE, INSERT, SELECT, SHOW VIEW, UPDATE ON pliddb.* TO plidbackend@localhost;

CREATE TABLE `plantlist` (
  `email` varchar(50) NOT NULL, 
  `planttype` varchar(50) NOT NULL, 
  `startdate` date,
  `plantid` varchar(50) NOT NULL, 
  PRIMARY KEY (`plantid`, `email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

