-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: mask_db
-- Время создания: Июн 16 2022 г., 16:18
-- Версия сервера: 8.0.29
-- Версия PHP: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `mask_base`
--

-- --------------------------------------------------------

--
-- Структура таблицы `result_shots`
--

CREATE TABLE `result_shots` (
  `id` int NOT NULL,
  `link` varchar(2083) CHARACTER SET utf8mb3 COLLATE utf8_general_ci NOT NULL,
  `title` text NOT NULL,
  `shot_number` text NOT NULL,
  `frame_duration` text NOT NULL,
  `image` longtext NOT NULL,
  `block_id` varchar(200) NOT NULL,
  `user_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `result_shots`
--
ALTER TABLE `result_shots`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `result_shots`
--
ALTER TABLE `result_shots`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
