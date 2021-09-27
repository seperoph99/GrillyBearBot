<?php include('server.php') ?>
<!DOCTYPE html>
<!--Calling required external source javascript-->
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  



<html>
<head>
<!--Title and stylesheet of the webpage-->
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="styles.css">
	
<!--Accordion script for the webpage-->
  <script>
  $( function() {
    $( "#accordion" ).accordion();
  } );
  </script>
</head>
<body>
<!--Manually setting the background image of the webpage-->
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
		<div class = "Login"><a class="active" href = "login.php">Login</a>
		<div class = "Register"><a href = "register.php">Sign Up</a>
</div>
	</div>
	</div>
	</div>
	
	<form method="post" action="login.php">

		<?php include('errors.php'); ?>
<!--Setting up the form for the login-->
  </body>
		<div class="input-group">
			<label>Username</label>
			<input type="text" name="username" >
		</div>
		<div class="input-group">
			<label>Password</label>
			<input type="password" name="password">
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="login_user">Login</button>
		</div>


		</div>
		<br></br>
	



</body>

</html>