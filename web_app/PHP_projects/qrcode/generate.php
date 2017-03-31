<!DOCTYPE html>
<html>
    <head>
        <style>
            #info{
                width:300px;
                height:300px;
            }
        </style>
    </head>
    <body>
       <?php 
if(isset($_POST['generate_text']))
{
 include('phpqrcode/qrlib.php'); 
 $text=$_POST['qr_text'];
 $folder="images/";
 $file_name="qr.png";
 $file_name=$folder.$file_name;
 QRcode::png($text,$file_name);
 echo"<img". "id='info' src='images/qr.png '>";
 
 //To Display Code Without Storing
 QRcode::png($text);
} 
?>
    </body>
</html>


