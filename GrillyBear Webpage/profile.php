<?php 
	session_start(); 

	if (!isset($_SESSION['username'])) {
		$_SESSION['msg'] = "You must log in first";
		header('location: login.php');
	}

	if (isset($_GET['logout'])) {
		session_destroy();
		unset($_SESSION['username']);
		header("location: login.php");
	}

?>
<!DOCTYPE html>
<html>
<head>

	<title>Home</title>
	<link rel="stylesheet" type="text/css" href="styles.css">
	  <link rel="stylesheet" href="https://code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">
  <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
  <script src="https://code.jquery.com/ui/1.10.4/jquery-ui.js"></script>

	<script src="js/tabcontent.js"></script>
	<script src="js/tablesort.js"></script>
	<script src="js/dialogbox.js"></script>
</head>
<body>
	<div class="header">
		<h2>Home Page</h2>
	</div>
	<div class="content">

		<!-- notification message -->
		<?php if (isset($_SESSION['success'])) : ?>
			<style>
			body {
			  background-image: url('Background.gif');
			}
			</style>
			<div class="error success" >
				<h3>
					<?php 
						echo $_SESSION['success']; 
						unset($_SESSION['success']);
					?>
				</h3>
			</div>
		<?php endif ?>

		<!-- logged in user information -->
		<?php  if (isset($_SESSION['username'])) : ?>
		<div id="shadowBox">
			<p class = "rainboww rainbow_text_animated">Welcome <strong><?php echo $_SESSION['username']; ?></strong></p>
			</div>
			<p><strong>This is the profile page for the girlly bear bot. It will have functionallity in the future but for now its just a placeholder.</strong></p>

<div id="dialog"></div>
<style>
.dialog{
    width: 100px;
    max-width: 200px;
    white-space: nowrap;
    overflow: hidden;
	background-image: linear-gradient(to right,#393261, #379683);
	color: #FFF; font-weight: bold;
	height: 40px;
	padding:0;
}
</style>

			
			
			<p> <a href="profile.php?logout='1'" style="color: red;">logout</a> </p>
			
		<?php endif ?>
	</div>
		
</body>
</html>