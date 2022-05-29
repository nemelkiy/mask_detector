<?php

require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection('localhost', 5672, 'admin', 'Admin1234');
$channel = $connection->channel();

$channel->queue_declare('result_shots', false, false, false, false);

echo " [*] Waiting for messages. To exit press CTRL+C\n";

$callback = function ($msg) {
    echo $msg->body, "\n";
};
  
$channel->basic_consume('result_shots', '', false, true, false, false, $callback);
  
while ($channel->is_open()) {
      $channel->wait();
}