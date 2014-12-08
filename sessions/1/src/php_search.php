<?php

$search = '';
if (isset($_POST['s']) && !empty($_POST['s'])) {
	$search = $_POST['s'];
}

if($_POST['submit'])
{
	include 'DB.php';
	$sql = 'SELECT * FROM session1
			WHERE firstname LIKE %:firstname% 
			OR lastname  LIKE %:lastname%';

	$stmt = $db->prepare($sql);
	$stmt->bindValue(":firstname", $search, PDO::PARAM_STR);
	$stmt->bindValue(":lastname", $search, PDO::PARAM_STR);
	$stmt->execute();

	$rows = $stmt->PDO::FETCH_ASSOC);
	print_r($rows);
}

?>