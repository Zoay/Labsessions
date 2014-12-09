`<?php

$output = '';

if (isset($_POST['s'])) {
	$search = $_POST['s'];
	$search = preg_replace("#[^a-z0-9]#i", "", $search);

	include 'DB.php';

	$sql = "SELECT * FROM session1
			WHERE firstname LIKE CONCAT ('%', :firstname, '%')
			OR    lastname LIKE CONCAT ('%', :lastname, '%')";

	$stmt = $db->prepare($sql);
	$stmt->bindValue(':firstname', $search, PDO::PARAM_STR);
	$stmt->bindValue(':lastname', $search, PDO::PARAM_STR);
	$stmt->execute();

	$rows = $stmt->fetch(PDO::FETCH_ASSOC);
	echo ' count ' . count($rows);
	print_r($rows);

	if (count($rows) != 0) {
		while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
			$firstname = $row['firstname'];
			$lastname = $row['lastname'];
			$output .= $firstname . ' ' . $lastname;
		}
	} else {
		echo 'Element searched was not found...';
	}
	echo $output;
	$stmt->closeCursor();
}

?>