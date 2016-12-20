<!DOCTYPE html>
<html> 
	<head>
		<title>Bob’s Auto Parts - Order Results</title> 
	</head>
<body>
	<h1>Bob’s Auto Parts</h1> <h2>Order Results</h2>
	<?php

	$tireqty = $_POST['tireqty'];
	$oilqty = $_POST['oilqty'];
	$sparkqty = $_POST['sparkqty'];
	$address = $_POST['address'];
	$DOCUMENT_ROOT = $_SERVER['DOCUMENT_ROOT'];
	$date = date('H:i, jS F Y');

	define('TIREPRICE', 100); 
	define('OILPRICE', 10); 
	define('SPARKPRICE', 4);

	echo "<p>Order processed at "; 
	echo date('H:i, jS F Y'); 
	echo "</p>";

	$totalqty = 0;
	$totalqty = $tireqty + $oilqty + $sparkqty;
	echo "Items ordered: ".$totalqty."<br/>";

	if($totalqty == 0){
		echo "You did not order any items <br/>";
	} else {
		if ($tireqty > 0){
			echo $tireqty.' tires<br/>';
		} 

		if($oilqty > 0){
			echo "$oilqty bottles of oil<br/>";
		}

		if ($sparkqty > 0){
			echo "$sparkqty spark plugs<br/>";
		}
		echo "<br/>";
	}

	$totalamount = 0.00;
	$totalamount = ($tireqty * TIREPRICE) + ($oilqty * OILPRICE) + ($sparkqty * SPARKPRICE);
	$totalamount = number_format($totalamount,2,,'.',' ');
	echo "<p>Total of order is $".$totalamount."</p>";
	echo "<p>Address to ship to is ".$address."</p>";
	$outputString = $date."\t".$tireqty." tires \t".$oilqty." oil\t"
	.$sparkqty." spark plugs\t\$".$totalamount."\t".$address."\n";

	@ $fp = fopen("$DOCUMENT_ROOT/.../orders.txt",'ab');
	flock($fp,LOCK_EX);
	if(!$fp){
		echo "<p><strong> Your order could not be processed at this time.
		Please try again later.</strong></p></body></html>"; exit;
	}
	fwrite($fp, $outputstring, strlen($outputstring)); flock($fp, LOCK_UN);
	fclose($fp);

	echo "<p>Order written.</p>";
	
	 ?> 

	</body>
</html>