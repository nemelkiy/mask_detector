<?php
//Параметры для баз данных
$dbhost = "mask_db";
//$dbhost = "127.0.0.1";
$dbport = 7003;
$dbuser = "root";
$dbpass = "root";
$dbname = "mask_base";

//Соединение с БД
$link = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname) or die('Connect');

/**
 * console mode
 */

//$link = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname, $dbport) or die('Connect');

mysqli_query($link, "SET NAMES 'utf8';");
mysqli_query($link, "SET CHARACTER SET 'utf8';");

$blockId = $_POST['block_id'];
$userId = $_POST['user_id'];


$user_query = "INSERT INTO user_table (user_id, rId) VALUES (
    \"" . $userId ."\",
    \"".$blockId."\"
)";

$user_result = mysqli_query($link, $user_query);

echo $blockId;

require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection('rabbitmq', 5672, 'admin', 'Admin1234');


$channel = $connection->channel();

$channel->queue_declare('result_shots', false, false, false, false);

$callback = function ($msg) {

    if($msg->body){

        global $blockId;
        global $link;
        global $userId;

        $jObj = json_decode($msg->body);

        $query = "INSERT INTO result_shots (link, title, shot_number, frame_duration, image, block_id, user_id) VALUES (
            \"".$jObj->link."\",
            \"".$jObj->title."\",
            ".$jObj->shot_number.",
            ".$jObj->frame_duration.",
            \"".$jObj->data."\",
            \"".$blockId."\",
            \"" . $userId ."\")";
        
        $result = mysqli_query($link, $query);

        if(!$result){
            echo 'Got problems with query';
        }else{
            echo 'Query is writen';
        }
        echo 'Queue is works';
    } 
};
  
$channel->basic_consume('result_shots', '', false, true, false, false, $callback);

while ($channel->is_open()) {
      $channel->wait();
}

echo 'finished';