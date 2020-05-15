<?php
// get ID of the foodworks to be read
$id = isset($_GET['id']) ? $_GET['id'] : die('ERROR: missing ID.');
 
// include database and object files
include_once 'config/database.php';
include_once 'src/foodworks.php';
 
// get database connection
$database = new Database();
$db = $database->getConnection();
 
// prepare objects
$foodworks = new Foodworks($db);
 
// set ID property of foodworks to be read
$foodworks->id = $id;
 
// read the details of foodworks to be read
$foodworks->readOne();

// set page headers
$page_title = "Product";
include_once "header.php";
 
// read products button
echo "<div class='right-button-margin'>";
    echo "<a href='index.php' class='btn btn-primary pull-right'>";
        echo "<span class='glyphicon glyphicon-list'></span> Products";
    echo "</a>";
echo "</div>";

// HTML table for displaying a product details
echo "<table class='table table-hover table-responsive table-bordered'>";
 
    echo "<tr>";
        echo "<td>Title</td>";
        echo "<td>{$foodworks->title}</td>";
    echo "</tr>";
 
    echo "<tr>";
        echo "<td>price</td>";
        echo "<td>${$foodworks->price}</td>";
    echo "</tr>";
 
    echo "<tr>";
        echo "<td>description</td>";
        echo "<td>{$foodworks->description}</td>";
    echo "</tr>";
 
    echo "<tr>";
        echo "<td>image_url</td>";
        echo "<td>{$foodworks->image_url}</td>";
    echo "</tr>";
 
echo "</table>";
 
// set footer
include_once "footer.php";
?>