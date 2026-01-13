-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 13, 2026 at 06:27 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory_logs`
--

CREATE TABLE `inventory_logs` (
  `id` int(11) NOT NULL,
  `tanggal` date DEFAULT NULL,
  `supplier` varchar(255) DEFAULT NULL,
  `kategori` varchar(100) DEFAULT NULL,
  `item` varchar(255) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `satuan` varchar(50) DEFAULT NULL,
  `harga` decimal(15,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory_logs`
--

INSERT INTO `inventory_logs` (`id`, `tanggal`, `supplier`, `kategori`, `item`, `qty`, `satuan`, `harga`, `created_at`) VALUES
(2, '2025-12-22', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Resleting JP YEE', 1, 'lusin', 21000.00, '2026-01-13 16:48:05'),
(3, '2025-12-22', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Scotlight', 1, 'roll', 100000.00, '2026-01-13 16:48:05'),
(4, '2025-12-22', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Perekat', 1, 'roll', 28500.00, '2026-01-13 16:48:05'),
(5, '2025-12-22', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Retsleting Jaket Lion', 1, 'lusin', 36000.00, '2026-01-13 16:48:05'),
(6, '2025-12-22', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Retsleting CFC', 1, 'lusin', 15550.00, '2026-01-13 16:48:05'),
(7, '2025-12-22', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Gt Dexlan', 1, 'biji', 17500.00, '2026-01-13 16:48:05'),
(8, '2025-12-16', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Kancing', 1, 'gross', 35000.00, '2026-01-13 16:48:05'),
(9, '2025-12-13', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Retsleting CFC', 1, 'lusin', 16000.00, '2026-01-13 16:48:05'),
(10, '2025-12-13', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Retsleting Lion', 1, 'lusin', 36000.00, '2026-01-13 16:48:05'),
(11, '2025-12-09', 'Sinar Surya', 'Bahan Baku Utama', 'Kain Jet Black', 1, 'pcs', 28500.00, '2026-01-13 16:48:05'),
(12, '2025-12-09', 'UD. Menang Kancing Surabaya', 'Bahan Baku Utama', 'Kain Jet Black Wool Peach', 1, 'm', 28500.00, '2026-01-13 16:48:05'),
(13, '2025-12-09', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Kancing Hias', 1, 'pack', 40000.00, '2026-01-13 16:48:05'),
(14, '2025-12-09', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Resleting JP YEE 10', 1, 'lusin', 17500.00, '2026-01-13 16:48:05'),
(15, '2025-12-08', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Kancing Lili', 1, 'gross', 32500.00, '2026-01-13 16:48:05'),
(16, '2025-12-04', 'Toko Konveksi (KF)', 'Bahan Pendukung', 'Retsleting Jepang', 1, 'lusin', 20000.00, '2026-01-13 16:48:05'),
(17, '2025-12-03', 'Toko Meme', 'Bahan Pendukung', 'Benang Jahit Putra', 1, 'lusin', 19000.00, '2026-01-13 16:48:05'),
(18, '2025-12-03', 'Toko Meme', 'Bahan Pendukung', 'Kancing Mutiara', 1, 'gross', 21000.00, '2026-01-13 16:48:05'),
(19, '2025-12-03', 'Toko Meme', 'Bahan Pendukung', 'Karet Elastic', 1, 'roll', 33000.00, '2026-01-13 16:48:05'),
(20, '2025-11-25', 'Toko Konveksi (KF)', 'Bahan Pendukung', 'Scotlight Rompi', 1, 'roll', 55000.00, '2026-01-13 16:48:05'),
(21, '2025-11-22', 'Flores Jaya', 'Bahan Baku Utama', 'Kain Jala Mesh Biru', 1, 'm', 75000.00, '2026-01-13 16:48:05'),
(22, '2025-11-21', 'Toko Bahan Textile Trijaya', 'Bahan Baku Utama', 'Kain Union', 1, 'yard', 28000.00, '2026-01-13 16:48:05'),
(23, '2025-11-19', 'CV. Mimi Fashion', 'Bahan Baku Utama', 'Kain Jala Fashion', 1, 'kg', 62000.00, '2026-01-13 16:48:05'),
(24, '2025-11-18', 'Bintang Mas', 'Bahan Pendukung', 'Scotlight Wajik', 1, 'roll', 60000.00, '2026-01-13 16:48:05'),
(25, '2025-11-13', 'Nurakaci Store', 'Bahan Baku Utama', 'Kain Jala Double Mesh Orange', 1, 'm', 47000.00, '2026-01-13 16:48:05'),
(26, '2025-11-13', 'Nurakaci Store', 'Bahan Baku Utama', 'Kain Jala Double Mesh Biru', 1, 'm', 47000.00, '2026-01-13 16:48:05'),
(27, '2025-11-13', 'Nurakaci Store', 'Bahan Baku Utama', 'Kain Jala Double Mesh Merah', 1, 'm', 47000.00, '2026-01-13 16:48:05'),
(28, '2025-09-17', 'UD. Karunia Sejahtera', 'Bahan Baku Utama', 'Kain TRM', 1, 'm', 21000.00, '2026-01-13 16:48:05'),
(29, '2025-09-01', 'Bintang Mas', 'Bahan Baku Utama', 'Kain Keras TK', 1, 'roll', 425000.00, '2026-01-13 16:48:05'),
(30, '2025-08-23', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Benang Yamalon', 1, 'lusin', 18000.00, '2026-01-13 16:48:05'),
(31, '2025-08-23', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Retsleting', 1, 'lusin', 7000.00, '2026-01-13 16:48:05'),
(32, '2025-08-22', 'Toko Kain Hongkong', 'Bahan Baku Utama', 'Kain Toyobo', 1, 'm', 25000.00, '2026-01-13 16:48:05'),
(33, '2025-08-12', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Kancing', 1, 'gross', 10000.00, '2026-01-13 16:48:05'),
(34, '2025-07-24', 'PT. Knitto Tekstil Indonesia', 'Bahan Pendukung', 'Manset CVC Pique 24s - Abu Muda', 0, 'lg', 51980.00, '2026-01-13 16:48:05'),
(35, '2025-07-23', 'PT. Knitto Tekstil Indonesia', 'Bahan Baku Utama', 'CVC Pique Hexagon 24s - Abu Muda', 1, 'kg', 107000.00, '2026-01-13 16:48:05'),
(36, '2025-07-23', 'PT. Knitto Tekstil Indonesia', 'Bahan Baku Utama', 'CVC Pique Hexagon 24s - Putih Bluish', 1, 'kg', 102000.00, '2026-01-13 16:48:05'),
(37, '2025-07-23', 'PT. Knitto Tekstil Indonesia', 'Bahan Pendukung', 'Krah CVC Pique 24s - Abu Muda', 1, 'kg', 77970.00, '2026-01-13 16:48:05'),
(38, '2025-07-19', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Retsleting', 1, 'lusin', 16650.00, '2026-01-13 16:48:05'),
(39, '2025-07-18', 'Toko Konveksi (KF)', 'Bahan Pendukung', 'Kancing', 1, 'gross', 38500.00, '2026-01-13 16:48:05'),
(40, '2025-07-17', 'Sinar Surya', 'Bahan Baku Utama', 'TC Olive Pramuka', 1, 'roll', 1050000.00, '2026-01-13 16:48:05'),
(41, '2025-07-08', 'Toko Bahan Textile Trijaya', 'Bahan Baku Utama', 'Kain Japan Dril', 1, 'yard', 35000.00, '2026-01-13 16:48:05'),
(42, '2025-07-04', 'Sinar Surya', 'Bahan Baku Utama', 'Kain American Macan', 1, 'm', 26000.00, '2026-01-13 16:48:05'),
(43, '2025-07-01', 'PT Knitto Tekstil Indonesia', 'Bahan Baku Utama', 'Kain Commbed 24s Navy', 1, 'kg', 109000.00, '2026-01-13 16:48:05'),
(44, '2025-07-01', 'PT Knitto Tekstil Indonesia', 'Bahan Baku Utama', 'Kain Commbed 24s Mustard', 1, 'kg', 106000.00, '2026-01-13 16:48:05'),
(45, '2025-07-01', 'PT. Knitto Tekstil Indonesia', 'Bahan Pendukung', 'Krah CVC Pique 24s - Abu Muda', 1, 'kg', 124000.00, '2026-01-13 16:48:05'),
(46, '2025-06-25', 'PT. Domivatex Lestari Abadi', 'Bahan Baku Utama', 'Kain Pablo Escobar', 1, 'yard', 20000.00, '2026-01-13 16:48:05'),
(47, '2025-06-25', 'PT. Domivatex Lestari Abadi', 'Bahan Baku Utama', 'Kain Toyobo', 1, 'yard', 16500.00, '2026-01-13 16:48:05'),
(48, '2025-06-19', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Kancing BK', 1, 'mass', 49500.00, '2026-01-13 16:48:05'),
(49, '2025-06-19', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Hak Talon GBL', 1, 'dus', 38500.00, '2026-01-13 16:48:05'),
(50, '2025-06-17', 'Sinar Surya', 'Bahan Baku Utama', 'TC Olive Putih', 1, 'roll', 1550000.00, '2026-01-13 16:48:05'),
(51, '2025-06-05', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Kancing Polisi Besar', 1, 'gross', 41500.00, '2026-01-13 16:48:05'),
(52, '2025-05-22', 'Toko Konveksi (KF)', 'Bahan Baku Utama', 'Kain Kapas Kuralon', 1, 'roll', 167500.00, '2026-01-13 16:48:05'),
(53, '2025-05-22', 'Toko Konveksi (KF)', 'Bahan Baku Utama', 'Kain Furing', 1, 'roll', 477500.00, '2026-01-13 16:48:05'),
(54, '2025-05-22', 'Toko Konveksi (KF)', 'Bahan Pendukung', 'Hak Talon Polos', 1, 'doss', 35000.00, '2026-01-13 16:48:05'),
(55, '2025-05-22', 'Toko Konveksi (KF)', 'Bahan Pendukung', 'Retsleting GPO', 1, 'lusin', 28000.00, '2026-01-13 16:48:05'),
(56, '2025-05-15', 'Toko Konveksi (KF)', 'Bahan Baku Utama', 'Kain Keras Megatop', 1, 'roll', 467500.00, '2026-01-13 16:48:05'),
(57, '2025-05-15', 'Toko Konveksi (KF)', 'Bahan Pendukung', 'Karet P12 A Putih', 1, 'kg', 46000.00, '2026-01-13 16:48:05'),
(58, '2025-05-15', 'Toko Konveksi (KF)', 'Bahan Pendukung', 'Kancing CSS 33 (30)', 1, 'lusin', 41500.00, '2026-01-13 16:48:05'),
(59, '2025-05-03', 'Cahaya Surabaya', 'Bahan Baku Utama', 'Kain Lurik', 1, 'm', 48000.00, '2026-01-13 16:48:05'),
(60, '2025-05-03', 'UD. Karunia Sejahtera', 'Bahan Baku Utama', 'Kain Toyobo Premium', 1, 'roll', 1350000.00, '2026-01-13 16:48:05'),
(61, '2025-04-24', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Resleting JP YEE', 1, 'pcs', 4200.00, '2026-01-13 16:48:05'),
(62, '2025-04-23', 'Toko Kain Sutratex', 'Bahan Baku Utama', 'Kain Centini', 1, 'm', 30000.00, '2026-01-13 16:48:05'),
(63, '2025-04-22', 'MM', 'Bahan Pendukung', 'Kancing', 1, 'gross', 21000.00, '2026-01-13 16:48:05'),
(64, '2025-04-22', 'MM', 'Bahan Pendukung', 'Tali Karet KT', 1, 'roll', 14000.00, '2026-01-13 16:48:05'),
(65, '2025-04-22', 'MM', 'Bahan Pendukung', 'Benang Jahit Putra', 1, 'lusin', 19000.00, '2026-01-13 16:48:05'),
(66, '2025-04-16', 'Esteva Indonesia', 'Bahan Baku Utama', 'Kain Milano', 1, 'roll', 1215000.00, '2026-01-13 16:48:05'),
(67, '2025-03-12', 'Subur Jaya Lumintu', 'Bahan Pendukung', 'HS Putih', 1, 'kg', 55000.00, '2026-01-13 16:48:05'),
(68, '2025-03-12', 'UB. Intisari Jaya', 'Bahan Pendukung', 'Selang Bening', 1, 'm', 4000.00, '2026-01-13 16:48:05'),
(69, '2025-03-04', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Kancing Safari', 1, 'gross', 16500.00, '2026-01-13 16:48:05'),
(70, '2025-03-03', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Retsleting', 1, 'pcs', 2500.00, '2026-01-13 16:48:05'),
(71, '2025-02-15', 'CV.  Prima berkah sejati', 'ATK', 'Buku Nota', 1, 'pcs', 6200.00, '2026-01-13 16:48:05'),
(72, '2025-02-04', 'Jaya Santosa', 'ATK', 'Kran Air Soligen', 1, 'pcs', 43000.00, '2026-01-13 16:48:05'),
(73, '2025-02-03', 'UD. Menang Kancing Surabaya', 'Bahan Pendukung', 'Kancing Celana', 1, 'gross', 10000.00, '2026-01-13 16:48:05'),
(74, '2025-02-03', 'UD. Aries Jaya', 'ATK', 'Lampu', 1, 'set', 156000.00, '2026-01-13 16:48:05'),
(75, '2025-02-03', 'Toko Enny Nur', 'ATK', 'Baterai ABC Alkaline', 1, 'pack', 14000.00, '2026-01-13 16:48:05'),
(76, '2025-02-03', 'Toko Kertas Sari Agung', 'ATK', 'Kertas HVS 70 Gr', 1, 'lembar', 3500.00, '2026-01-13 16:48:05'),
(77, '2024-04-23', 'Toko Kain Sutratex', 'Bahan Baku Utama', 'Kain Satin', 1, 'm', 30000.00, '2026-01-13 16:48:05');

-- --------------------------------------------------------

--
-- Table structure for table `stock_outs`
--

CREATE TABLE `stock_outs` (
  `id` int(11) NOT NULL,
  `tanggal` date DEFAULT NULL,
  `item` varchar(255) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `satuan` varchar(50) DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stock_outs`
--

INSERT INTO `stock_outs` (`id`, `tanggal`, `item`, `qty`, `satuan`, `keterangan`, `created_at`) VALUES
(1, '2026-01-14', 'Baterai ABC Alkaline', 1, 'lusin', 'Seragam SMA', '2026-01-13 17:19:23'),
(2, '2026-01-14', 'Benang Yamalon', 1, 'lusin', 'Seragam SD', '2026-01-13 17:20:10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inventory_logs`
--
ALTER TABLE `inventory_logs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock_outs`
--
ALTER TABLE `stock_outs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `inventory_logs`
--
ALTER TABLE `inventory_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- AUTO_INCREMENT for table `stock_outs`
--
ALTER TABLE `stock_outs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
