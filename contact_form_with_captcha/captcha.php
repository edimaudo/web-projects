<?php
 
session_start();
 
$string = '';
 
for ($i = 0; $i < 5; $i++) {
    $string .= chr(rand(97, 122));
}
 
$_SESSION['random_code'] = $string;

$dir = 'fonts/';
 
$image = imagecreatetruecolor(170, 60);
$black = imagecolorallocate($image, 0, 0, 0);
$color = imagecolorallocate($image, 200, 100, 90); // red
$white = imagecolorallocate($image, 255, 255, 255);

imagefilledrectangle($image,0,0,200,100,$white);
imagettftext($image, 30, 0, 10, 40, $alt, $dir."arial.ttf", $_SESSION['rand_code']);