-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 08, 2016 at 04:53 PM
-- Server version: 5.6.32
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python`
--

-- --------------------------------------------------------

--
-- Table structure for table `taula`
--

CREATE TABLE `taula` (
  `time` int(13) DEFAULT NULL,
  `user` varchar(20) DEFAULT NULL,
  `tweet` varchar(140) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `taula`
--

INSERT INTO `taula` (`time`, `user`, `tweet`) VALUES
(1385419969, 'Volodymyr', 'welcom to my tutorial'),
(1385419985, 'Alexandr', 'Hi, thaks!'),
(1385419994, 'Volodymyr', 'How are you !');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
