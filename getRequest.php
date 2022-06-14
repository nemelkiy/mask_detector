<?php

//Параметры для баз данных
$dbhost = "mask_db";
$dbuser = "root";
$dbpass = "root";
$dbname = "mask_base";

//Соединение с БД
$link = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname) or die('Connect');

mysqli_query($link, "SET NAMES 'cp1251';");
mysqli_query($link, "SET CHARACTER SET 'cp1251';");

require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection('172.18.0.3', 5672, 'admin', 'Admin1234');


$channel = $connection->channel();

$channel->queue_declare('result_shots', false, false, false, false);

$callback = function ($msg) {
    $mesage = json_decode($msg->body);

    print_r($mesage);
};
  
$channel->basic_consume('result_shots', '', false, true, false, false, $callback);
  
while ($channel->is_open()) {
      $channel->wait();
}