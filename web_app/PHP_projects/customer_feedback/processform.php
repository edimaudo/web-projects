<?php

//form input
$name = trim($_POST['name']);
$email = trim($_POST['email']);
$feedback = addslashes(trim($_POST['feedback']));
$submit = $_POST["submit"];

//send email
$toaddress = "edimaudo@gmail.com";
$subject = "Feedback from web site";
$mailcontent = nl2br("Customer name: ".$name."\n". "Customer email: ".$email."\n"."Customer comments:\n".$feedback."\n"); 

$fromaddress = "From: ".$email;

//invoke mail() function to send mail
mail($toaddress, $subject, $mailcontent, $fromaddress);

?>

<html>
<head>
<title>Bob's Auto Parts - Feedback Submitted</title> </head>
<body>
<h1>Feedback submitted</h1>
<p>Your feedback has been sent.</p>
</body>
</html>