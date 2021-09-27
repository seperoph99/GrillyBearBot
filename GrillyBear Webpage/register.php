<?php include('server.php') ?>
<!DOCTYPE html>
<html>
<!--Title and stylesheet of the webpage-->
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
<!--Manually setting the background image of the webpage itself-->
<style>
body {
  background-image: url('Background.gif');
}
</style>

<!--Setting the nav bar-->

		<div class="header">
		<div class="topnav">
		<a href="index.html">Home</a>
		<a href="Bot_Commands.html">Bot Commands</a>
		<!-- <a href="SourceCode.html">Source Code</a>
		<a href="download.html">Downloads</a>
		<a href="contact_us.html">Contact Us</a>
		<a href="Javascript.html">Extra Javascript</a> -->
		<div class = "Login"><a href = "login.php">Login</a>
		<div class = "Register"><a class="active" href = "register.php">Sign Up</a>
</div>
	</div>
	</div>
	</div>
			<!--Starting a post method for the register php-->
			<form method="post" action="register.php">

				<?php include('errors.php'); ?>
				<!--Setting required external javascript files-->
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
			<script src="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js"></script>

			<!--Setting up the form for the registration of the webpage-->
		
		<div class="input-group">
			<label>Username</label>
			<input type="text" name="username" value="<?php echo $username; ?>">
		</div>
		<div class="input-group">
			<label>Email</label>
			<input type="email" name="email" value="<?php echo $email; ?>">
		</div>
		<div class="input-group">
			<label>Password</label>
			<input type="password" name="password_1">
		</div>
		<div class="input-group">
			<label>Confirm password</label>
			<input type="password" name="password_2">
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="reg_user">Register</button>
		</div>
		<!--Linking the login page to sign in with if hit register page by mistake-->

	</form>
</body>
</html>