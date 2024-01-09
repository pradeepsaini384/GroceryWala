-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 23, 2023 at 08:03 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `juhacks`
--

-- --------------------------------------------------------

--
-- Table structure for table `bakery`
--

CREATE TABLE `bakery` (
  `p_id` varchar(20) NOT NULL,
  `p_name` varchar(30) NOT NULL,
  `vendor_name` varchar(30) NOT NULL,
  `price` int(6) NOT NULL,
  `category` text NOT NULL,
  `sub_category` text NOT NULL,
  `img_path` varchar(70) NOT NULL,
  `time` timestamp(6) NOT NULL DEFAULT current_timestamp(6),
  `offer_price` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bakery`
--

INSERT INTO `bakery` (`p_id`, `p_name`, `vendor_name`, `price`, `category`, `sub_category`, `img_path`, `time`, `offer_price`) VALUES
('Bk-9', 'britannia toastea premium bake', 'Royal Bakers', 70, 'bakery', 'daily', '/ju_images/bakery/bakery1.jpg', '0000-00-00 00:00:00.000000', 65),
('Bk_1', 'cashew biscuits karachi', 'Royal Bakers', 100, 'Bakery', 'popular', '/ju_images/bakery/bakery2.jpeg', '0000-00-00 00:00:00.000000', 0),
('Bk_16', 'Hershey\'s Chocolate Syrup', 'Royal Bakers', 200, 'bakery', 'popular', '/ju_images/bakery/bakery3.jpg', '0000-00-00 00:00:00.000000', 150),
('Bk_2', 'parle happy happy choco chip c', 'Royal Baker', 20, 'bakery', 'daily', '/ju_images/bakery/bakery4.jpg', '0000-00-00 00:00:00.000000', 16),
('Bk_4', 'nature whole wheet bread', 'Royal Baker', 40, 'bakery', 'daily', '/ju_images/bakery/bakery5.jpg', '0000-00-00 00:00:00.000000', 33),
('Bk_5', 'Britannia 5050 Potazos Crisps', 'Royal Baker', 30, 'bakery', 'popular', '/ju_images/bakery/bakery6.jpg', '0000-00-00 00:00:00.000000', 25),
('Bk_6', 'Kalory Brown Bread', 'Royal Bakers', 40, 'bakery', 'daily', '/ju_images/bakery/bakery7.jpg', '2023-02-22 08:01:44.000000', 34),
('B_5', 'Sunfeast Dark Fantasy Original', 'Royal Baker', 30, 'bakery', 'popular', '/ju_images/bakery/bakery8.jpg', '2023-02-14 08:14:15.000000', 25),
('B_56', 'Britannia 100% Veg Choco Chill', 'Royal Baker', 30, 'bakery', 'popular', '/ju_images/bakery/bakery9.jpg', '2023-02-14 08:14:15.000000', 5),
('P_4', 'Britannia Treat Vanilla Creme ', 'Royal Baker', 40, 'bakery', 'recommended', '/ju_images/bakery/bakery10.jpg', '2023-02-05 08:17:31.000000', 37);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bakery`
--
ALTER TABLE `bakery`
  ADD PRIMARY KEY (`p_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
