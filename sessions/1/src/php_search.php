<?php

if (isset($_POST['s'])) {
	$search = $_POST['s'];
	$search = preg_replace("#[^a-z0-9]#i", "", $search);

	include 'DB.php';

	$sql = "SELECT * FROM session1
			WHERE firstname LIKE CONCAT ('%', :firstname, '%')
			OR    lastname LIKE CONCAT ('%', :lastname, '%')";

	$stmt = $db->prepare($sql);
	$stmt->bindParam(':firstname', $search, PDO::PARAM_STR);
	$stmt->bindParam(':lastname', $search, PDO::PARAM_STR);
	$stmt->execute();

	$output = '';

	//Processing the result
	while (($row = $stmt->fetch(PDO::FETCH_ASSOC)) != false) {
		//print_r($row);
		$fn = $row['firstname'];
		$ln = $row['lastname'];

		$output .= '<div>' . $fn . ' ' . $ln . '</div>';
	}

	if (strlen($output) == 0) {
		$output .= 'User Not Found!';
	}

	print($output);
	$stmt->closeCursor();
}

?>