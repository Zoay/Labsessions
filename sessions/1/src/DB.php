<?php

$servername = 'localhost';
$dbname = 'zoay_labsessions';

$user = 'root';
$pwd = 'root';

$dsn = "mysql:host=$servername;dbname=$dbname";

try
{
	$db = new PDO($dsn, $user, $pwd);
	// Set the PDO Error Mode to exception
	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

} catch (PDOException $e) {
	echo $e->getMessage();
}

?>