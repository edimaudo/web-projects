<!DOCTYPE html>
<html>
    <body>
        <?php
        $target_dir = "filemetasize/";
        $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
        $uploadOk = 1;
        if(isset($_POST["submit"])) {
            $size =  $_FILES["fileToUpload"]["size"];
            $arr = array('size ' => $size);
            echo json_encode($arr);
        }
        ?>
    </body>
</html>