<!DOCTYPE html>
<html>
<head>
	<title>Bob's Freight</title>
</head>
<body>
	<table border="0" cellpadding="3">
		<tr>
			<td bgcolor="#cccccc" align="center">Distance</td>
			<td bgcolor="#cccccc" align="center">Cost</td>
		</tr>
		<tr>
		<?
			$distance = 50;
			while($distance <=250){
				echo "<tr>
					 <td align=\"right\">".$distance."</td>
					 <td align=\"right\">".($distance / 10)."</td>
					 </tr>\n";
				$distance+=50;
			}
		?>
	</table>
</body>
</html>