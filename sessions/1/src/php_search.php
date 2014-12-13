<?php

if (isset($_POST['qq'])) {
	$search = $_POST['qq'];
	$search = preg_replace("#[^a-z0-9]#i", "", $search);

	include 'DB.php';

	$sql = "SELECT * FROM session1
			WHERE firstname LIKE CONCAT ('%', :firstname, '%')
			OR    lastname LIKE CONCAT ('%', :lastname, '%')";

	$stmt = $db->prepare($sql);
	$stmt->bindValue(':firstname', $search, PDO::PARAM_STR);
	$stmt->bindValue(':lastname', $search, PDO::PARAM_STR);
	$stmt->execute();

	$output = '';
	$result = array();
	$arr = array();

	//Processing the result
	while (($row = $stmt->fetch(PDO::FETCH_ASSOC)) != false) {
		$firstname = $row['firstname'];
		$lastname = $row['lastname'];

		//$output .= $firstname . ' ' . $lastname;
		$arr['firstname'] = $firstname;
		$arr['lastname'] = $lastname;

		array_push($result, $arr);
	}

	/*if (strlen($output) == 0) {
	$output .= 'No results found!';
	}*/

	echo json_encode($result);
	$stmt->closeCursor();
	$stmt = NULL;
}
?>