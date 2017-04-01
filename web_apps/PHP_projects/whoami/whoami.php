<!doctype html>
<html>
    <body>
        <?php
        $ipaddress = $_SERVER['HTTP_CLIENT_IP']?$_SERVER['HTTP_CLIENT_IP']:($_SERVER['HTTP_X_FORWARDE‌​D_FOR']?$_SERVER['HTTP_X_FORWARDED_FOR']:$_SERVER['REMOTE_ADDR']);
        $language = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);
        $software = php_uname('s');
        $arr = array ('IP Address'=>$ipaddress,'Language'=> $language,'OS'=> $software);
        echo json_encode($arr);
        ?>
    </body>
</html>