
<html>
<head>
<link type="text/css" rel="stylesheet" href="style.css"/>
</head>
<body>
<div id="wrapper">

<div id="convert_div">
    <h1>Currency Converter</h1>
<form method="post"action="index.php">
 <input type="number" name="amount" placeholder="Enter Amount" required>
 <select name="convert_from">
  <option  value="INR">Indian Rupee</option>
  <option  value="USD">US Dollar</option>
  <option  value="SGD">Singapore Dollar</option>
  <option  value="EUR">Euro</option>
  <option  value="AED">UAE Dirham</option>
  <option  value="CAD">Canadian Dollar</option>
 </select>
 <select name="convert_to">
  <option  value="INR">Indian Rupee</option>
  <option  value="USD">US Dollar</option>
  <option  value="SGD">Singapore Dollar</option>
  <option  value="EUR">Euro</option>
  <option  value="AED">UAE Dirham</option>
  <option  value="CAD">Canadian Dollar</option>
 </select>
 <br>
 <input type="submit" name="convert_currency" value="Convert Currency">
</form>
</div>
<?php
function currency_converter($from,$to,$amount)
{
 $url = "http://www.google.com/finance/converter?a=$amount&from=$from&to=$to"; 
 
 $request = curl_init(); 
 $timeOut = 0; 
 curl_setopt ($request, CURLOPT_URL, $url); 
 curl_setopt ($request, CURLOPT_RETURNTRANSFER, 1); 
 
 curl_setopt ($request, CURLOPT_USERAGENT,"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)"); 
 curl_setopt ($request, CURLOPT_CONNECTTIMEOUT, $timeOut); 
 $response = curl_exec($request); 
 curl_close($request); 
 
 return $response;
} 

if(isset($_POST['convert_currency']))
{
 $amount=$_POST['amount'];
 $from=$_POST['convert_from'];
 $to=$_POST['convert_to'];
	
 $rawData = currency_converter($from,$to,$amount);
 $regex = '#\<span class=bld\>(.+?)\<\/span\>#s';
 preg_match($regex, $rawData, $converted);
 $result = $converted[0];
 echo $result;
}
?>
</div>
</body>
</html>