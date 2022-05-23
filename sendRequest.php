<?php

require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'admin', 'Admin1234');
$channel = $connection->channel();

$channel->queue_declare('movie_requests', false, false, false, false);

$msg = new AMQPMessage('{  
    "link":"https://www.youtube.com/watch?v=UgAJOBNsk9Q",  
    "fps": 1  
}');
$channel->basic_publish($msg, '', 'movie_requests');

echo " [x] Sending request\n";

$channel->close();
$connection->close();