<?php

$serverName = 'localhost';
$dbname = 'zoay_labsessions';
$user = 'root';
$pwd = 'root';

try
{
	$db = new PDO("mysql:host=$serverName;dbname=$dbname", $user, $pwd);
	// Set the PDO Error Mode to exception
	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

	//echo "Connected to the database!";

} catch (PDOException $e) {
	echo $e->getMessage();
}

?>