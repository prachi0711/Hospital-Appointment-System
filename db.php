<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbName = "management";

$con = mysqli_connect($servername, $username, $password, $dbName);

if (mysqli_connect_errno()){
    echo "failed to connect";
    exit();
}
echo "connection success";
?>