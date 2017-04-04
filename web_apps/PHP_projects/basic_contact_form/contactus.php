<?php

if(isset($_POST['sendmail'])){
	$name = $_POST['name'];

	$email = $_POST['email'];

	$website = $_POST['website'];

	$subject = $_POST['subject'];

	$message = $_POST['message'];

	$to = "you@programmer.com"; 

	if(empty($name) OR empty($email) OR empty($subject) OR empty($message)){

		echo "<div class='errors'>Sorry, You must fill the required fields<strong>(*)</strong></div>";

	}else{

		@mail($to,$subject,$message,"From: $name  <$email>");

		echo "<div class='done'>Email has been sent, we will get back to you ASAP!</strong></div>";

	}
}

?>