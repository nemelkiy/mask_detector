<?php



$video_link = $_POST['video_link'];
$video_frame = $_POST['video_frame'];

require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('rabbitmq', 5672, 'admin', 'Admin1234');
$channel = $connection->channel();

$channel->queue_declare('movie_requests', false, false, false, false);

$msg = new AMQPMessage('{  
    "link":"' . $video_link . '",  
    "fps": ' . $video_frame . '
}');
$channel->basic_publish($msg, '', 'movie_requests');

echo "sanded";

$channel->close();
$connection->close();

//https://www.youtube.com/watch?v=UgAJOBNsk9Q - Origin video
//https://www.youtube.com/watch?v=fgCzQ0BNQDM - Cutted video