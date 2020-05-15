<?php
// check if value was posted
if($_POST){
 
    // include database and object file
    include_once 'config/database.php';
    include_once 'src/foodworks.php';
 
    // get database connection
    $database = new Database();
    $db = $database->getConnection();
 
    // prepare foodworks object
    $foodworks = new Foodworks($db);
     
    // set foodworks id to be deleted
    $foodworks->id = $_POST['object_id'];
     
    // delete the foodworks
    if($foodworks->delete()){
        echo "Object was deleted.";
    }
     
    // if unable to delete the foodworks
    else{
        echo "Unable to delete object.";
    }
}
?>