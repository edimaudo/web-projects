<html>
<body>
    <?php
    $input = $_POST['info'];
    $errorinfo = "not a date or timestamp";
    
    if ( is_numeric($input) && (int)$input == $input ) {
       echo '{ unix: '. $input . ', natural: ' .date('Y-m-d H:i:s', (int)$input).'}';   
    }  else {
        echo "<i>$errorinfo</i>";
    }
    ?>
</body>
</html>