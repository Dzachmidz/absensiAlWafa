-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 12, 2026 at 03:29 AM
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
-- Database: `absensialwafa`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add siswa', 7, 'add_siswa'),
(26, 'Can change siswa', 7, 'change_siswa'),
(27, 'Can delete siswa', 7, 'delete_siswa'),
(28, 'Can view siswa', 7, 'view_siswa'),
(29, 'Can add absensi', 8, 'add_absensi'),
(30, 'Can change absensi', 8, 'change_absensi'),
(31, 'Can delete absensi', 8, 'delete_absensi'),
(32, 'Can view absensi', 8, 'view_absensi'),
(33, 'Can add rfid log', 9, 'add_rfidlog'),
(34, 'Can change rfid log', 9, 'change_rfidlog'),
(35, 'Can delete rfid log', 9, 'delete_rfidlog'),
(36, 'Can view rfid log', 9, 'view_rfidlog'),
(37, 'Can add kelas', 10, 'add_kelas'),
(38, 'Can change kelas', 10, 'change_kelas'),
(39, 'Can delete kelas', 10, 'delete_kelas'),
(40, 'Can view kelas', 10, 'view_kelas'),
(41, 'Can add waktu operasional', 11, 'add_waktuoperasional'),
(42, 'Can change waktu operasional', 11, 'change_waktuoperasional'),
(43, 'Can delete waktu operasional', 11, 'delete_waktuoperasional'),
(44, 'Can view waktu operasional', 11, 'view_waktuoperasional');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(2, 'pbkdf2_sha256$600000$PdjFVv06U9492iKMoHSjLZ$MJpX5pkGOA/zB1kBrCkJSmEcij+pLgeWvrBRv03t7QA=', '2026-01-11 15:50:14.052234', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2026-01-09 08:12:11.526195');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2026-01-09 08:12:24.749622', '1', 'adm', 3, '', 4, 2),
(2, '2026-01-11 15:51:03.697520', '1', 'ACHMAD FAHMI AL HAFIDZ - 2026-01-11 (Hadir)', 3, '', 8, 2),
(3, '2026-01-11 15:52:45.401458', '2', 'ACHMAD FAHMI AL HAFIDZ - 2026-01-11 (Terlambat)', 3, '', 8, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(8, 'userapp', 'absensi'),
(10, 'userapp', 'kelas'),
(9, 'userapp', 'rfidlog'),
(7, 'userapp', 'siswa'),
(11, 'userapp', 'waktuoperasional');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-01-09 08:04:36.847842'),
(2, 'auth', '0001_initial', '2026-01-09 08:04:37.063352'),
(3, 'admin', '0001_initial', '2026-01-09 08:04:37.103248'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-01-09 08:04:37.106320'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-01-09 08:04:37.108853'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-01-09 08:04:37.128880'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-01-09 08:04:37.147089'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-01-09 08:04:37.156262'),
(9, 'auth', '0004_alter_user_username_opts', '2026-01-09 08:04:37.158874'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-01-09 08:04:37.171320'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-01-09 08:04:37.172388'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-01-09 08:04:37.181624'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-01-09 08:04:37.190871'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-01-09 08:04:37.199439'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-01-09 08:04:37.208978'),
(16, 'auth', '0011_update_proxy_permissions', '2026-01-09 08:04:37.211967'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-01-09 08:04:37.223559'),
(18, 'sessions', '0001_initial', '2026-01-09 08:04:37.242742'),
(19, 'userapp', '0001_initial', '2026-01-09 08:04:37.283298'),
(20, 'userapp', '0002_absensi_created_at', '2026-01-09 08:18:13.483278'),
(21, 'userapp', '0003_rfidlog', '2026-01-09 14:59:26.770221'),
(22, 'userapp', '0004_kelas_alter_siswa_rfid_uid_alter_siswa_kelas', '2026-01-09 15:17:27.884458'),
(23, 'userapp', '0005_waktuoperasional_alter_kelas_options', '2026-01-09 15:39:59.605815'),
(24, 'userapp', '0006_absensi_status_kehadiran_kelas_jadwal_masuk_akhir_and_more', '2026-01-11 15:29:25.762034');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('pn9q0mhtam9qgia1mh3ede3yu6fxcnjp', '.eJxVjDsOwjAQBe_iGlnG618o6TlDtN5dcADZUpxUiLtDpBTQvpl5LzXiupRx7TKPE6uTsurwu2Wkh9QN8B3rrWlqdZmnrDdF77TrS2N5nnf376BgL986owuBBK-cTXSRAqCnIzoUcRaY0LJPaHLwDlLEOATI4BKZwdhABtT7AwW2N-s:1vexhm:LMvtbR-247Z7LYuf6uldipT4QCVSTiTk_Y77j1YMeiE', '2026-01-25 15:50:14.053194');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_absensi`
--

CREATE TABLE `userapp_absensi` (
  `id` bigint(20) NOT NULL,
  `tanggal` date NOT NULL,
  `hari` varchar(20) NOT NULL,
  `jam_masuk` time(6) NOT NULL,
  `jam_keluar` time(6) DEFAULT NULL,
  `siswa_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status_kehadiran` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userapp_absensi`
--

INSERT INTO `userapp_absensi` (`id`, `tanggal`, `hari`, `jam_masuk`, `jam_keluar`, `siswa_id`, `created_at`, `status_kehadiran`) VALUES
(3, '2026-01-11', 'Sunday', '22:52:49.595231', NULL, 1, '2026-01-11 15:52:49.595258', 'Terlambat'),
(4, '2026-01-12', 'Monday', '08:31:42.795278', NULL, 1, '2026-01-12 01:31:42.795311', 'Terlambat'),
(5, '2026-01-12', 'Monday', '08:31:53.473250', NULL, 2, '2026-01-12 01:31:53.473268', 'Terlambat');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_kelas`
--

CREATE TABLE `userapp_kelas` (
  `id` bigint(20) NOT NULL,
  `nama_kelas` varchar(50) NOT NULL,
  `jadwal_masuk_akhir` time(6) NOT NULL,
  `jadwal_masuk_mulai` time(6) NOT NULL,
  `jadwal_pulang_akhir` time(6) NOT NULL,
  `jadwal_pulang_mulai` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userapp_kelas`
--

INSERT INTO `userapp_kelas` (`id`, `nama_kelas`, `jadwal_masuk_akhir`, `jadwal_masuk_mulai`, `jadwal_pulang_akhir`, `jadwal_pulang_mulai`) VALUES
(1, 'Al Quran', '07:15:00.000000', '06:00:00.000000', '17:00:00.000000', '14:00:00.000000'),
(2, 'Pasca 2', '07:15:00.000000', '06:00:00.000000', '17:00:00.000000', '14:00:00.000000'),
(3, 'Pasca 1', '07:15:00.000000', '06:00:00.000000', '17:00:00.000000', '14:00:00.000000'),
(4, 'Pasca 3', '07:15:00.000000', '06:00:00.000000', '17:00:00.000000', '14:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_rfidlog`
--

CREATE TABLE `userapp_rfidlog` (
  `id` bigint(20) NOT NULL,
  `rfid_uid` varchar(50) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `keterangan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userapp_rfidlog`
--

INSERT INTO `userapp_rfidlog` (`id`, `rfid_uid`, `timestamp`, `status`, `keterangan`) VALUES
(1, '2795884089', '2026-01-11 15:00:49.541424', 'unknown', 'Kartu tidak terdaftar'),
(2, '3143215044', '2026-01-11 15:01:00.924789', 'success', 'Selamat Datang (Telat), ACHMAD FAHMI AL HAFIDZ - Al Quran'),
(3, '3143215044', '2026-01-11 15:01:15.239070', 'success', 'Selamat Jalan, ACHMAD FAHMI AL HAFIDZ - Al Quran'),
(4, '3143215044', '2026-01-11 15:50:20.949756', 'success', 'Hati-hati di jalan, ACHMAD FAHMI AL HAFIDZ - Al Quran'),
(5, '3143215044', '2026-01-11 15:50:28.333658', 'success', 'Hati-hati di jalan, ACHMAD FAHMI AL HAFIDZ - Al Quran'),
(6, '3143215044', '2026-01-11 15:51:11.025093', 'success', 'Selamat Datang (Telat), ACHMAD FAHMI AL HAFIDZ - Al Quran'),
(7, '3143215044', '2026-01-11 15:51:17.977215', 'success', 'Selamat Jalan (Telat Jemput), ACHMAD FAHMI AL HAFIDZ - Al Quran'),
(8, '3143215044', '2026-01-11 15:52:49.596392', 'success', 'Selamat Datang (Telat), ACHMAD FAHMI AL HAFIDZ - Al Quran'),
(9, '3143215044', '2026-01-12 01:31:42.796332', 'success', 'Selamat Datang (Telat), ACHMAD FAHMI AL HAFIDZ - Al Quran'),
(10, '2795884089', '2026-01-12 01:31:53.474197', 'success', 'Selamat Datang (Telat), Silva Febiola - Pasca 1');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_siswa`
--

CREATE TABLE `userapp_siswa` (
  `id` bigint(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `nik` varchar(20) NOT NULL,
  `kelas_id` bigint(20) DEFAULT NULL,
  `no_telepon` varchar(15) NOT NULL,
  `rfid_uid` varchar(50) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userapp_siswa`
--

INSERT INTO `userapp_siswa` (`id`, `nama`, `nik`, `kelas_id`, `no_telepon`, `rfid_uid`, `created_at`) VALUES
(1, 'ACHMAD FAHMI AL HAFIDZ', '3515072009020015', 1, '082233254044', '3143215044', '2026-01-09 15:24:59.351867'),
(2, 'Silva Febiola', '1249590105810385', 3, '12345678912', '2795884089', '2026-01-12 01:29:05.366909'),
(3, 'MUHAMMAD HAFIDZ SYAFIUDDIN', 'IMP.1768182591.1', 4, '-', NULL, '2026-01-12 01:49:51.019487'),
(4, 'BIMA SANJAYA ', 'IMP.1768182591.2', 4, '-', NULL, '2026-01-12 01:49:51.020991'),
(5, 'DIO ALVARO JALES YUDHA', 'IMP.1768182591.3', 4, '-', NULL, '2026-01-12 01:49:51.021740'),
(6, 'MUHAMAD RAFFA RAMADHANI', 'IMP.1768182591.4', 4, '-', NULL, '2026-01-12 01:49:51.024757'),
(7, 'BINTANG KHANZA AL-MAIRA', 'IMP.1768182591.5', 4, '-', NULL, '2026-01-12 01:49:51.025359'),
(8, 'ATIQOH FAIRUZ KHALISHA', 'IMP.1768182591.6', 4, '-', NULL, '2026-01-12 01:49:51.025804'),
(9, 'MUHAMMAD HANIF SYAFIUDDIN', 'IMP.1768182610.1', 2, '-', NULL, '2026-01-12 01:50:10.914964'),
(10, 'AKBAR MUHAMMAD RASYID ALFATIH', 'IMP.1768182610.2', 2, '-', NULL, '2026-01-12 01:50:10.916258'),
(11, 'NAFIZA APRILIA HERIANSYAH ', 'IMP.1768182610.3', 2, '-', NULL, '2026-01-12 01:50:10.916763'),
(12, 'MOCHAMMAD NICO SHOBRON QOLBY', 'IMP.1768182610.4', 2, '-', NULL, '2026-01-12 01:50:10.917188'),
(13, 'JAFNI SAAFIA ANINDITA IRSYAD', 'IMP.1768182610.5', 2, '-', NULL, '2026-01-12 01:50:10.917538'),
(14, 'GILANG AYYASY IMRON', 'IMP.1768182610.6', 2, '-', NULL, '2026-01-12 01:50:10.917881'),
(15, 'NISHWA TAHTA ELMAHIRA ', 'IMP.1768182610.7', 2, '-', NULL, '2026-01-12 01:50:10.918389'),
(16, 'MUHAMMAD NABIL BAHTIAR', 'IMP.1768182610.8', 2, '-', NULL, '2026-01-12 01:50:10.918904'),
(17, 'ARSYAKA VIRENDRA IRAWAN', 'IMP.1768182610.10', 2, '-', NULL, '2026-01-12 01:50:10.919380'),
(18, 'LUH JINGGA SHAZFA AZKADINA', 'IMP.1768182610.11', 2, '-', NULL, '2026-01-12 01:50:10.919836'),
(19, 'CLARIESSA LEXANDRA SIDQIA DEWI', 'IMP.1768182610.12', 2, '-', NULL, '2026-01-12 01:50:10.920350'),
(20, 'DEVAN RAFANDRA ALFARIZI', 'IMP.1768182610.13', 2, '-', NULL, '2026-01-12 01:50:10.920784'),
(21, 'MUHAMMAD AZIZAN NASIR ASFA', 'IMP.1768182610.14', 2, '-', NULL, '2026-01-12 01:50:10.921175'),
(22, 'ROSYIDAH KHOIRUN NISA\'', 'IMP.1768182610.15', 2, '-', NULL, '2026-01-12 01:50:10.921597'),
(23, 'GINANJAR SURYO PRANOTO', 'IMP.1768182610.16', 2, '-', NULL, '2026-01-12 01:50:10.921954'),
(24, 'MUHAMMAD AZZAM AL FATIH', 'IMP.1768182610.17', 2, '-', NULL, '2026-01-12 01:50:10.922273'),
(25, 'DIWANGGA JAYAWARDANA', 'IMP.1768182610.18', 2, '-', NULL, '2026-01-12 01:50:10.922570'),
(26, 'MUHAMMAD HAFIDZ SYAFIUDDIN', 'IMP.1768182625.1', 3, '-', NULL, '2026-01-12 01:50:25.649707'),
(27, 'MUKHAMMAD FURQON ALFARIZI', 'IMP.1768182625.2', 3, '-', NULL, '2026-01-12 01:50:25.651016'),
(28, 'AZKA ADREENA MUSTOFA', 'IMP.1768182625.3', 3, '-', NULL, '2026-01-12 01:50:25.651778'),
(29, 'FATIN SAHIRA AZZAHRA', 'IMP.1768182625.4', 3, '-', NULL, '2026-01-12 01:50:25.652395'),
(30, 'ANINDITA NASYWA RAKHIA PUTRI', 'IMP.1768182625.5', 3, '-', NULL, '2026-01-12 01:50:25.653019'),
(31, 'SHAFIYYAH KAYLA AGATHA', 'IMP.1768182625.6', 3, '-', NULL, '2026-01-12 01:50:25.653646'),
(32, 'PUTRI HAFIZAH', 'IMP.1768182625.7', 3, '-', NULL, '2026-01-12 01:50:25.654354'),
(33, 'TIAR FAHRI MOHAMMAD PUTRA UTAMA', 'IMP.1768182625.8', 3, '-', NULL, '2026-01-12 01:50:25.654979'),
(34, 'NAURA ANASTASYA ZAINURI', 'IMP.1768182625.9', 3, '-', NULL, '2026-01-12 01:50:25.655525'),
(35, 'PASHA SATYA DHARMA RAMADHAN', 'IMP.1768182625.10', 3, '-', NULL, '2026-01-12 01:50:25.656126'),
(36, 'DISA SAPUTRA', 'IMP.1768182625.11', 3, '-', NULL, '2026-01-12 01:50:25.656701'),
(37, 'AISYAH FITRIA FARHANAH', 'IMP.1768182625.12', 3, '-', NULL, '2026-01-12 01:50:25.657241'),
(38, 'DZAKIYYAH AKIFA SAKHI', 'IMP.1768182625.13', 3, '-', NULL, '2026-01-12 01:50:25.657833'),
(39, 'ALYA ZAHRA ZAFIRAH ', 'IMP.1768182625.14', 3, '-', NULL, '2026-01-12 01:50:25.658441'),
(40, 'WIRDA ZANNUBA RAHMAH', 'IMP.1768182625.15', 3, '-', NULL, '2026-01-12 01:50:25.659029'),
(41, 'DARREL FAYYADHI ALMAIR', 'IMP.1768182625.16', 3, '-', NULL, '2026-01-12 01:50:25.659867'),
(42, 'DAFHINA ASHADIYA RAZEETA', 'IMP.1768182625.17', 3, '-', NULL, '2026-01-12 01:50:25.660407'),
(43, 'DEDE BAIHAQI FAHMI IDRIS ', 'IMP.1768182625.18', 3, '-', NULL, '2026-01-12 01:50:25.660977'),
(44, 'ADIBAH KEISHA UFAIRAH ', 'IMP.1768182625.19', 3, '-', NULL, '2026-01-12 01:50:25.661552'),
(45, 'NAUFALYN AQITA INARA', 'IMP.1768182625.20', 3, '-', NULL, '2026-01-12 01:50:25.662051'),
(46, 'ADINDA KIRANA PUTRI', 'IMP.1768182625.21', 3, '-', NULL, '2026-01-12 01:50:25.662665'),
(47, 'SHAFIYA MEI SYADINDA', 'IMP.1768182625.22', 3, '-', NULL, '2026-01-12 01:50:25.663196');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_waktuoperasional`
--

CREATE TABLE `userapp_waktuoperasional` (
  `id` bigint(20) NOT NULL,
  `jam_masuk_mulai` time(6) NOT NULL,
  `jam_masuk_akhir` time(6) NOT NULL,
  `jam_pulang_mulai` time(6) NOT NULL,
  `jam_pulang_akhir` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userapp_waktuoperasional`
--

INSERT INTO `userapp_waktuoperasional` (`id`, `jam_masuk_mulai`, `jam_masuk_akhir`, `jam_pulang_mulai`, `jam_pulang_akhir`) VALUES
(1, '06:00:00.000000', '08:00:00.000000', '12:00:00.000000', '17:00:00.000000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `userapp_absensi`
--
ALTER TABLE `userapp_absensi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userapp_absensi_siswa_id_700e4ef2_fk_userapp_siswa_id` (`siswa_id`);

--
-- Indexes for table `userapp_kelas`
--
ALTER TABLE `userapp_kelas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nama_kelas` (`nama_kelas`);

--
-- Indexes for table `userapp_rfidlog`
--
ALTER TABLE `userapp_rfidlog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userapp_siswa`
--
ALTER TABLE `userapp_siswa`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nik` (`nik`),
  ADD UNIQUE KEY `rfid_uid` (`rfid_uid`),
  ADD KEY `userapp_siswa_kelas_id_5d92775e` (`kelas_id`);

--
-- Indexes for table `userapp_waktuoperasional`
--
ALTER TABLE `userapp_waktuoperasional`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `userapp_absensi`
--
ALTER TABLE `userapp_absensi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `userapp_kelas`
--
ALTER TABLE `userapp_kelas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userapp_rfidlog`
--
ALTER TABLE `userapp_rfidlog`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `userapp_siswa`
--
ALTER TABLE `userapp_siswa`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `userapp_waktuoperasional`
--
ALTER TABLE `userapp_waktuoperasional`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `userapp_absensi`
--
ALTER TABLE `userapp_absensi`
  ADD CONSTRAINT `userapp_absensi_siswa_id_700e4ef2_fk_userapp_siswa_id` FOREIGN KEY (`siswa_id`) REFERENCES `userapp_siswa` (`id`);

--
-- Constraints for table `userapp_siswa`
--
ALTER TABLE `userapp_siswa`
  ADD CONSTRAINT `userapp_siswa_kelas_id_5d92775e_fk_userapp_kelas_id` FOREIGN KEY (`kelas_id`) REFERENCES `userapp_kelas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
