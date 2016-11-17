-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 10, 2016 at 12:07 PM
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
-- Table structure for table `link`
--

CREATE TABLE `link` (
  `time` int(13) DEFAULT NULL,
  `linn_txt` varchar(540) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `link`
--

INSERT INTO `link` (`time`, `linn_txt`) VALUES
(1478779497, 'https://auto.ria.com/auto_volkswagen_caravelle_18411915.html'),
(1478779497, 'https://auto.ria.com/auto_ford_ecosport_18504240.html'),
(1478779497, 'https://auto.ria.com/auto_mercedes-benz_e-class_18504544.html'),
(1478779497, 'https://auto.ria.com/auto_skoda_superb_18395495.html'),
(1478779497, 'https://auto.ria.com/auto_mercedes-benz_b-180_17747786.html'),
(1478779497, 'https://auto.ria.com/auto_mercedes-benz_e-class_18508291.html'),
(1478779497, 'https://auto.ria.com/auto_audi_a6_18476415.html'),
(1478779497, 'https://auto.ria.com/auto_ford_ecosport_18504293.html'),
(1478779497, 'https://auto.ria.com/auto_mercedes-benz_e-class_18476953.html'),
(1478779497, 'https://auto.ria.com/auto_mercedes-benz_e-class_17713436.html');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
