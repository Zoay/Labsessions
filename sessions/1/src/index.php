<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Creating a search</title>
	<style type="text/css">
	.wrapper{
		width:50%;
	}
	</style>
</head>
<body>
	<div class="wrapper">
		<center>
			<h2>Instant Search </h2>
			<div>
				<form method="post" action="">
					<input type="text" name="qq" id="srch" size="50" placeholder="Search..." />
					<!--<input type="submit" value="Search" />-->
				</form>
			</div>
			<hr />
			<div id="result"></div>
		</center>
	</div>
	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<script src="../js/php_search.js"></script>
</body>
</html>