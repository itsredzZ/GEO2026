-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2026 at 05:44 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
-- Table structure for table `sales_summary_monthly`
--

CREATE TABLE `sales_summary_monthly` (
  `id` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `month_name` varchar(20) DEFAULT NULL,
  `item_count` int(11) DEFAULT NULL,
  `total_qty` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sales_summary_monthly`
--

INSERT INTO `sales_summary_monthly` (`id`, `year`, `month`, `month_name`, `item_count`, `total_qty`) VALUES
(1, 2023, 3, 'Mar', 1, 2000),
(2, 2023, 4, 'Apr', 1, 500),
(3, 2023, 6, 'Jun', 1, 1250),
(4, 2023, 7, 'Jul', 1, 152),
(5, 2023, 8, 'Aug', 2, 2848),
(6, 2023, 9, 'Sep', 11, 80462),
(7, 2023, 11, 'Nov', 2, 1440),
(8, 2023, 12, 'Dec', 1, 349),
(9, 2024, 3, 'Mar', 3, 3221),
(10, 2024, 4, 'Apr', 1, 103),
(11, 2024, 5, 'May', 1, 0),
(12, 2024, 6, 'Jun', 3, 2887),
(13, 2024, 7, 'Jul', 1, 155),
(14, 2024, 8, 'Aug', 1, 9),
(15, 2024, 9, 'Sep', 4, 3686),
(16, 2024, 10, 'Oct', 2, 70),
(17, 2024, 11, 'Nov', 1, 95),
(18, 2024, 12, 'Dec', 1, 49),
(19, 2025, 1, 'Jan', 2, 79),
(20, 2025, 2, 'Feb', 1, 1),
(21, 2025, 3, 'Mar', 8, 292),
(22, 2025, 4, 'Apr', 3, 88),
(23, 2025, 5, 'May', 25, 21405),
(24, 2025, 6, 'Jun', 5, 6968),
(25, 2025, 7, 'Jul', 5, 466),
(26, 2025, 8, 'Aug', 12, 12520),
(27, 2025, 9, 'Sep', 2, 159),
(28, 2025, 10, 'Oct', 3, 380),
(29, 2025, 11, 'Nov', 3, 364),
(30, 2025, 12, 'Dec', 1, 300);

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

-- --------------------------------------------------------

--
-- Table structure for table `tailors`
--

CREATE TABLE `tailors` (
  `id` int(11) NOT NULL,
  `kode_penjahit` varchar(50) DEFAULT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `nik` varchar(20) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `kecamatan` varchar(100) DEFAULT NULL,
  `usia` int(11) DEFAULT NULL,
  `kerapian` tinyint(1) DEFAULT NULL,
  `ketepatan_waktu` tinyint(1) DEFAULT NULL,
  `quantity` tinyint(1) DEFAULT NULL,
  `komitmen` tinyint(1) DEFAULT NULL,
  `spesialis` varchar(100) DEFAULT NULL,
  `status_keluarga_miskin` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tailors`
--

INSERT INTO `tailors` (`id`, `kode_penjahit`, `nama`, `nik`, `alamat`, `kecamatan`, `usia`, `kerapian`, `ketepatan_waktu`, `quantity`, `komitmen`, `spesialis`, `status_keluarga_miskin`) VALUES
(1, '3.24', 'Abdul Rozak', '3578171812650002', 'Sidomulyo II-C/5', 'Kenjeran', 61, 1, 1, 1, 1, 'Semua', 'Miskin Non Ekstrem'),
(2, '1.05', 'Afiah', '3578115706720006', 'Sidodadi 3 No. 1', 'Simokerto', 54, 1, 1, 1, 1, 'Semua', NULL),
(3, '1.2', 'Alfiyah', '3578165811710007', 'Wonokusumo Bhakti GG 2/28', 'Semampir', 55, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(4, '3.44', 'Anis Syayidah Ulfa', '3578115909790004', 'Jl. Pogot VI/26', 'Kenjeran', 47, 0, 0, 1, 1, 'Semua', 'Non Miskin'),
(5, '3.21', 'Aprilianti', '3578174604970001', 'Bulak Banteng Wetan XI/31', 'Kenjeran', 29, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(6, '3.26', 'Bambang Lukistianto', '3578111111640002', 'Kalilom Lor Indah Sedap Malam 14', 'Kenjeran', 62, 1, 1, 0, 1, NULL, 'Miskin Non Ekstrem'),
(7, '2.01', 'Dewi Ambar Arifiati', '3578046805820010', 'Deles buntu 1/5 Surabaya', 'Sukolilo', 44, 1, 1, 0, 1, NULL, 'Non Miskin'),
(8, '2.08', 'Dewi Munir Indratanti', '3578155407790001', 'Tambak Asri 29/83', 'Krembangan', 47, 0, 1, 1, 1, 'Semua', 'Non Miskin'),
(9, '2.09', 'Dewi Munir Indriyati', '3578155609770001', 'Tambak Asri 29/83', 'Krembangan', 49, 0, 1, 0, 1, NULL, 'Miskin Non Ekstrem'),
(10, '1.03', 'Diani Nanik Lestari', '3578056401710003', 'Simolawang 2/44b', 'Simokerto', 55, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(11, '4.06', 'Dyah Dwikora H.', '3578035012640001', 'Bakung 2b/ 34B', 'Rungkut', 61, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(12, '1.04', 'Endah Susanti', '3578115810770004', 'Granting Barat 105', 'Simokerto', 49, 0, 1, 0, 1, NULL, 'Miskin Non Ekstrem'),
(13, '3.14', 'Ernawati Ningsih', '3578175610820001', 'Pogot 9 b/3 a', 'Kenjeran', 44, 1, 1, 0, 1, NULL, 'Non Miskin'),
(14, '2.11', 'Evi Dharmawati', '357815402750004', 'Krembangan Jaya Sel 2C/8', 'Semampir', 51, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(15, '3.43', 'Faridah', '3578174406740004', 'Bulak Banteng Kidul 5/6', 'Kenjeran', 52, 0, 1, 0, 1, NULL, 'Miskin Non Ekstrem'),
(16, '1.13', 'Fatimatul Zaroh', '3578274610810001', 'Simorejo Sari B 13 No. 9A', 'Sukomanunggal', 45, 0, 1, 0, 1, NULL, 'Non Miskin'),
(17, '3.1', 'G. Kusnariati', '3578176709830002', 'Tambak wedi baru 13A dalam buntu no. 3', 'Kenjeran', 43, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(18, '2.07', 'Galuh Zahroh', '3578165009550000', 'Krembangan bakti 14/11', 'Krembangan', 71, 0, 0, 1, 0, NULL, 'Non Miskin'),
(19, '2.02', 'Hadak Mitharani', '3578135710820004', 'Jl. Medokan Semampir Indah Gg. 2 No. 1', 'Sukolilo', 44, 1, 1, 1, 1, NULL, 'Non Miskin'),
(20, '2.31', 'Hanafi', '3526142106710001', 'Karang Tembok 1/21-B', 'Semampir', 55, 1, 1, 1, 1, 'Seragam', NULL),
(21, '4.1', 'Hj. Umi Saroh', '3578036112560001', 'Kaliwaru GG Masjid No. 14', 'Rungkut', 70, 0, 1, 0, 1, NULL, 'Non Miskin'),
(22, '3.38', 'I\'anatus Sholiha', '3578295208730001', 'Sukolilo Larangan 3/23', 'Bulak', 53, 1, 1, 1, 1, 'Seragam', 'Non Miskin'),
(23, '2.24', 'Ina Indayati', '3578066801630001', 'Petemon 1 / 77 - H', 'Sawahan', 63, 1, 1, 0, 1, 'Semua', 'Pramiskin'),
(24, '4.07', 'Indah Handayani', '3578267112800003', 'Jl. Kalisari Damen No. 55-A', 'Mulyorejo', 46, 1, 1, 1, 1, 'Semua', 'Miskin Ekstrem'),
(25, '2.04', 'Isnaini', '3578095511750001', 'Gebang Wetan 1 No. 10', 'Sukolilo', 51, 0, 1, 0, 1, 'Seragam', 'Non Miskin'),
(26, '2.16', 'Istiqomah', '3578166206800004', 'Jl. Mrutu Kalianyar', 'Semampir', 41, 1, 1, 1, 1, NULL, 'Non Miskin'),
(27, '3.22', 'Katri', '3578176101650001', 'Tambak Wedi Masjid 6/10', 'Kenjeran', 61, 0, 1, 0, 1, NULL, 'Pramiskin'),
(28, '3.03', 'Khofifah', '3508086205880003', 'Tanah Merah Utara 1 No 12', 'Kenjeran', 38, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(29, '3.39', 'Khusnul Khotimah', '3578295403720001', 'Sukolilo Larangan 9/120', 'Bulak', 54, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(30, '1.11', 'Kikin Sukinah', '3578117112680002', 'Gembong 3/76', 'Simokerto', 58, 0, 0, 1, 0, 'Seragam', 'Non Miskin'),
(31, '2.26', 'Kuswati', '3578064601730000', 'Pakis 2 / 41B', 'Sawahan', 53, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(32, '3.2', 'Lailatul Wijayanti', '3578175004860003', 'Dukuh Bulak Banteng 46', 'Kenjeran', 40, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(33, '2.03', 'Lilis Sofiatain Nisa', '3578096906830003', 'Jl. Gebang Wetan No.32', 'Sukolilo', 43, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(34, '2.12', 'Luluk Ratnawati', '3578154412820001', 'Kalianak Timur BLK 2-D', 'Krembangan', 44, 0, 1, 1, 1, NULL, 'Non Miskin'),
(35, '1.07', 'M. Ali Mukhaidari', '3578110104800005', 'Simokerto 3/56', 'Simokerto', 46, 1, 1, 1, 1, 'Semua', 'Miskin Non Ekstrem'),
(36, '3.02', 'M. Prasanti Rahmawatun', '3578176711710002', 'Tanah Merah Sayur 7/19', 'Kenjeran', 55, 1, 1, 0, 1, NULL, 'Non Miskin'),
(37, '2.18', 'Mahlul Khamim', '3527061103800006', 'Wonokusumo Damai 4/23', 'Semampir', 46, 1, 1, 1, 1, 'Semua', NULL),
(38, '3.23', 'Maria Andriyana Leni', '3578174602740003', 'Tambak Wedi Komplek KMS 21B', 'Kenjeran', 52, 0, 1, 0, 1, NULL, 'Non Miskin'),
(39, '2.3', 'Maruf', '3578160301790005', 'Tenggumung Karya Lor 5 No. 10', 'Semampir', 47, 1, 1, 1, 1, 'Semua', NULL),
(40, '3.32', 'Maskur', '3578100107810017', 'Kapas Lor 1-C/16', 'Tambaksari', 45, 1, 1, 1, 1, 'Semua', NULL),
(41, '3.04', 'Maslacha', '3578177006570232', 'Tanah Merah Utara 1/1-A', 'Kenjeran', 69, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(42, '3.05', 'Mian', '3578123006650099', 'Randu Barat 1-B/38', 'Kenjeran', 61, 1, 1, 0, 1, 'Semua', NULL),
(43, '3.4', 'Mudawamah', '3578295101790001', 'Larangan sukolilo 2 no 26 RT 01 RW 01', 'Bulak', 47, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(44, '4.08', 'Mujianah', '3524096303770002', 'Jl. Kalisari I NO 69', 'Mulyorejo', 49, 1, 1, 0, 1, NULL, 'Miskin Non Ekstrem'),
(45, '1.16', 'Mujiono', '3578272212710001', 'Jl. Putat Gede Barat II/52', 'Sukomanunggal', 55, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(46, '1.14', 'Mujiyati', '3578274307830001', 'Simorejo Sari B 12 No. 2', 'Sukomanunggal', 43, 1, 1, 1, 1, 'Semua', 'Pramiskin'),
(47, '3.12', 'Muneri', '3576170806660001', 'Tanah Merah Utara 1/Tanah Kali Kedinding', 'Kenjeran', 60, 1, 1, 1, 1, 'Seragam', NULL),
(48, '2.27', 'Murdiana', '3578066508810002', 'Pakis Gunung 1-B/31', 'Sawahan', 45, 1, 0, 1, 1, 'Semua', 'Non Miskin'),
(49, '3.06', 'Muslicha', '3578144808550001', 'Tambak Wedi Indah Barat 2 D/ 16', 'Kenjeran', 71, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(50, '3.01', 'Nanik Fadilah', '3578177105790004', 'Kedinding Lor 2/136', 'Kenjeran', 47, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(51, '2.17', 'Neni Kuntarti', '3578165607820004', 'Wonosari 7/10', 'Semampir', 44, 1, 1, 0, 1, NULL, 'Non Miskin'),
(52, '4.16', 'Nina Ishariani', '3578086204770000', 'Mojoklanggru Lor 56', 'Gubeng', 49, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(53, '1.18', 'Nina Sulistyowati', '3578115703870001', 'Rusun Sumbo Blok E/101', 'Simokerto', 39, 1, 1, 0, 1, 'Semua', NULL),
(54, '4.09', 'Nunik Nurul Maslahah', '3578096212760005', 'Kejawan Gebang II/20', 'Sukolilo', 50, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(55, '3.16', 'Nur Aida', '3578174309650001', 'Tambak Wedi Tengah Timur 1A/3A', 'Kenjeran', 61, 1, 1, 0, 1, NULL, 'Miskin Non Ekstrem'),
(56, '1.02', 'Nur Hidayati', '3524265010800004', 'Wonosari Lor Baru 3/32', 'Semampir', 46, 0, 1, 0, 1, NULL, 'Non Miskin'),
(57, '4.02', 'Nurmahmuda', '3578265212810001', 'JL. Tempurejo No. 9/8', 'Mulyorejo', 45, 0, 1, 0, 1, NULL, 'Non Miskin'),
(58, '1.17', 'Nurhayati', '3578174910560003', 'Tanah Merah Sayur 3 Buntu No. 34', 'Kenjeran', 70, 1, 1, 0, 1, 'Semua', 'Pramiskin'),
(59, '1.15', 'Nurhayati', '3578125202820002', 'Rusun Sumbo Blok B/310', 'Simokerto', 44, 1, 1, 1, 1, NULL, NULL),
(60, '3.33', 'Nurul Fadilah', '3578116010790004', 'Tambak Segaran 1/47', 'Tambak Sari', 47, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(61, '1.19', 'Nurul Hidayati', '3578104709860002', 'Kalimas Barat 2/23', 'Pabean Cantian', 40, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(62, '1.1', 'Nurul Latifah', '3578167006750047', 'Tenggumung Wetan/Merpati 14', 'Semampir', 51, 1, 1, 0, 1, NULL, 'Non Miskin'),
(63, '3.07', 'Oemi Baidah', '3578174712650002', 'Tanah Merah Indah Sayur 3 no 8', 'Kenjeran', 61, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(64, '4.15', 'Ririn Rinantari', '3578035205720001', 'Tambak Medokan Ayu Kav. 11/4B', 'Rungkut', 54, 0, 1, 0, 1, NULL, NULL),
(65, '1.12', 'Rita', '3578275111630002', 'Simorejo Sari B 13 No. 11A', 'Sukomanunggal', 63, 0, 1, 0, 1, 'Seragam', 'Non Miskin'),
(66, '3.35', 'Rochmawati', '357810530980002', 'Jl. Labak Jaya Utara 5A/3', 'Kenjeran', 48, 0, 1, 0, 0, NULL, 'Non Miskin'),
(67, '3.09', 'Rusmini', '3578177006630311', 'Tanah Merah Sayur 5/36', 'Kenjeran', 63, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(68, '1.01', 'Saptorini', '3578126103700001', 'Tambak Gringsing Baru 3/3/3', 'Pabean Cantian', 56, 1, 1, 0, 1, 'Seragam', 'Pramiskin'),
(69, '1.21', 'Saptorini', '3578126103700001', 'Tambak Gringsing Baru 3/3/3', 'Pabean Cantian', 56, 1, 1, 0, 1, 'Seragam', NULL),
(70, '4.04', 'Shieny Suwito', '3578264507840003', 'Jl. Kalisari Timur 62', 'Mulyorejo', 42, 1, 1, 1, 1, 'Semua', 'Miskin Non Ekstrem'),
(71, '1.06', 'Siri', '3526131078110331', 'Kenjeran 4E/2', 'Simokerto', 42, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(72, '2.1', 'Siti Alfiyah', '3578167012710003', 'Bulak Sari 3/4', 'Semampir', 55, 0, 0, 0, 0, NULL, 'Pramiskin'),
(73, '2.05', 'Siti choiriyah', '3506154107790042', 'Gebang lor jl Kanoman 2 no 102 d', 'Sukolilo', 47, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(74, '4.03', 'Siti Fatimah', '3578036809720002', 'Kaliwaru 1/10', 'Rungkut', 54, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(75, '3.18', 'Siti Juhariyah', '3578174411880003', 'DK. Bulak Banteng Suropati 5-D/46', 'Kenjeran', 38, 1, 1, 1, 1, 'Semua', 'Miskin Non Ekstrem'),
(76, '4.01', 'Siti Muamanah', '3578264501850004', 'Jl. Tempurejo No. 9/19', 'Mulyorejo', 41, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(77, '2.22', 'Siti Muslimah Nuraini', '3578167006650416', 'Jl. Tenggumung Karya Lor 4c', 'Semampir', 61, 0, 1, 0, 1, 'Seragam', 'Non Miskin'),
(78, '1.09', 'Siti Zaenab', '3578116504840004', 'Sidodadi 10 14A', 'Simokerto', 42, 0, 1, 0, 1, 'Seragam', 'Miskin Non Ekstrem'),
(79, '3.08', 'Soeprijatin', '3578174510660002', 'Tanah Merah Sayur 7 No. 29', 'Kenjeran', 60, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(80, '1.08', 'Sri Mulyani', '3578117006730034', 'Sidoyoso 2/3/2', 'Simokerto', 53, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(81, '4.17', 'Sri Purwati', '3578086308670002', 'Mojoklanggru Lor 78-C', 'Gubeng', 59, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(82, '4.12', 'Sri Windu Utami', '3578266010750001', 'Manyar Sabrangan 5/38E', 'Mulyorejo', 51, 1, 1, 0, 1, 'Seragam', 'Pramiskin'),
(83, '3.28', 'Suaibah', '3578106010910002', 'Kapas Madya VI/131', 'Tambak Sari', 35, 1, 1, 0, 1, 'Seragam', NULL),
(84, '3.27', 'Sudartik', '3578104056610002', 'Kapas Madya 2-E-1/23', 'Tambak Sari', 65, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(85, '3.47', 'Sugiati', '3578175010730007', 'Kapas Lor Wetan 4 No. 7', 'Tambak Sari', 53, 1, 1, 0, 1, 'Seragam', NULL),
(86, '2.25', 'Suharning', '3578065708750004', 'Pakis 2/37-G', 'Sawahan', 51, 1, 1, 0, 1, 'Seragam', 'Pramiskin'),
(87, '3.15', 'Suharsih', '3578174105790001', 'Pogot 10/54', 'Kenjeran', 47, 1, 1, 1, 1, 'Semua', 'Pramiskin'),
(88, '3.42', 'Suhartini', '3578175805750001', 'Kedung Mangu 4D Buntu/6', 'Kenjeran', 50, 1, 1, 0, 1, 'Seragam', 'Pramiskin'),
(89, '3.17', 'Suliha', '3527084107752192', 'Tambak Wedi Baru 14/94A', 'Kenjeran', 46, 1, 1, 1, 1, 'Seragam', 'Non Miskin'),
(90, '3.13', 'Sumarti', '3578176001740001', 'Kedinding Lor Kamboja No. 92', 'Kenjeran', 52, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(91, '3.3', 'Sumarti', '357804404720008', 'Rangkah 6/29', 'Kenjeran', 54, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(92, '2.19', 'Tachtimul Khusna', '3578165609840003', 'Wonosari Lor Baru 2/1', 'Semampir', 42, 1, 1, 0, 1, NULL, 'Non Miskin'),
(93, '3.29', 'Titik Suparmi', '3578106101780001', 'Rangkah 6/29', 'Kenjeran', 48, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(94, '3.19', 'Tri Cahyani', '3578175801850002', 'Bulak Banteng Sekolahan 7-A/22', 'Kenjeran', 41, 1, 1, 1, 1, 'Seragam', 'Miskin Non Ekstrem'),
(95, '2.13', 'Tri Nofiati', '3578164311790002', 'Tenggumung Baru Selatan No. 71 F', 'Semampir', 47, 1, 0, 0, 1, 'Seragam', 'Miskin Non Ekstrem'),
(96, '2.06', 'Tri Ratnasari', '3578084912820003', 'Asempayung No 39', 'Sukolilo', 44, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(97, '3.25', 'Ubaidillah Andy', '3578161709770002', 'Bulak Banteng Madya 11/12', 'Kenjeran', 49, 1, 1, 1, 1, 'Seragam', 'Miskin Non Ekstrem'),
(98, '4.18', 'Umi Chanifah', '3578036708700001', 'Rungkut Kidul 3/48', 'Rungkut', 56, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(99, '2.2', 'Urifah Chasanah', '3578165311700003', 'Sidotopo Jaya 9/1', 'Semampir', 56, 0, 1, 1, 1, 'Seragam', 'Non Miskin'),
(100, '3.31', 'Warianti', '3516156201690001', 'Jl. Sidotopo Wetan Mulia GG 3 NO 56', 'Kenjeran', 57, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(101, '3.11', 'Wariyanti', '3516156201690001', 'Sidotopo Wetan Mulia Gg. 3/56', 'Kenjeran', 57, 1, 1, 0, 1, 'Seragam', NULL),
(102, '3.46', 'Waryadi', '3878101912710002', 'Ploso 9B-9', 'Tambak Sari', 55, 1, 1, 0, 1, 'Seragam', NULL),
(103, '4.05', 'Watik', '3578266011700003', 'Jl. Labansari 5-BLK', 'Mulyorejo', 56, 0, 1, 0, 1, NULL, 'Non Miskin'),
(104, '4.11', 'Winarty', '3578267006700004', 'Kalisari 62', 'Mulyorejo', 56, 1, 1, 1, 1, 'Seragam', 'Non Miskin'),
(105, '3.41', 'Wiwik Yuliani', '3578174111650004', 'Kedinding Lor GG Mawar No. 18', 'Kenjeran', 61, 1, 1, 0, 1, 'Semua', 'Non Miskin'),
(106, '2.15', 'Yuniati', '357816606740001', 'Tenggumung Karya Gg IB/1', 'Semampir', 52, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(107, '3.49', 'Jamilah', '3578175606750009', 'Takal, Kenjeran', 'Kenjeran', 51, 1, 1, 1, 1, 'Semua', 'Non Miskin'),
(108, '4.14', 'Lilik S.', '3578086510810002', 'Petung sewu, Gubeng', 'Gubeng', 45, 1, 1, 0, 1, 'Seragam', 'Non Miskin'),
(109, '4.13', 'Nur Faricha', '3578034808690004', 'Medokan ayu tambak gg 11', 'Rungkut', 57, 1, 1, 1, 1, 'Seragam', 'Non Miskin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inventory_logs`
--
ALTER TABLE `inventory_logs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales_summary_monthly`
--
ALTER TABLE `sales_summary_monthly`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock_outs`
--
ALTER TABLE `stock_outs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tailors`
--
ALTER TABLE `tailors`
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
-- AUTO_INCREMENT for table `sales_summary_monthly`
--
ALTER TABLE `sales_summary_monthly`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `stock_outs`
--
ALTER TABLE `stock_outs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tailors`
--
ALTER TABLE `tailors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=110;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
