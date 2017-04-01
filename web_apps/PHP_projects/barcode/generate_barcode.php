<!DOCTYPE html>
<html>
    <head>
<link href="barcode_style.css" type="text/css" rel="stylesheet"/>
</head>
<body>

<div id="wrapper">
<h1>Barcode generator</h1>
<div id="barcode_div">
 <form method="post" action="generate_barcode.php">
  <input type="text" name="barcode_text" required>
  <input type="submit" name="generate_barcode" value="GENERATE">
 </form>
 <?php
    if(isset($_POST['generate_barcode']))
    {
     $text=$_POST['barcode_text'];
     echo "<img id='barcode' alt='testing' src='barcode/barcode.php?codetype=Code39&size=40&text=".$text."&print=true'/>";
    }
 ?>
</div>

</div>


</body>
</html>