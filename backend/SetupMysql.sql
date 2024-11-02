DROP DATABASE IF EXISTS pliddb;

CREATE DATABASE pliddb /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

DROP USER IF EXISTS plidbackend@localhost;

CREATE USER plidbackend@localhost IDENTIFIED BY 'password';

USE pliddb;

GRANT DELETE, EXECUTE, INSERT, SELECT, SHOW VIEW, UPDATE ON pliddb.* TO plidbackend@localhost;

CREATE TABLE `user` (
  `password` varchar(50) NOT NULL, --
  `username` varchar(50) NOT NULL, --
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `plantinstance` (
  `owner` varchar(50) NOT NULL, --a foreign key to a user's username
  `planttype` varchar(50) NOT NULL, --one of 10 different preset strings
  `startdate` date --the starting date for a plant instance
  `plantid` int NOT NULL, --primary key for a plant instance
  PRIMARY KEY (`plantid`)
  KEY 'owner'
  CONSTRAINT `???` FOREIGN KEY (`owner`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

