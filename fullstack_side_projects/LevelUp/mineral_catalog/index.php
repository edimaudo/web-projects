<?php

// include database and object files
include_once "header.php";
include_once 'config/database.php';
include_once 'src/mineral.php';

 
// instantiate database and mineral object
$database = new Database();
$db = $database->getConnection();
 
$mineral = new Mineral($db);


$stmt = $mineral->readAll();
 
// specify the page where paging is used
$page_url = "index.php?";
 
// count total rows
$total_rows=$mineral->countAll();
 
// read_template.php controls how the mineral list will be rendered
include_once "read_template.php";
 
// layout_footer.php holds our javascript and closing html tags
include_once "footer.php";
?>