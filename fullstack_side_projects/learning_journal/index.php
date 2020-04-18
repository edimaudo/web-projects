<?php
// page given in URL parameter, default page is one
$page = isset($_GET['page']) ? $_GET['page'] : 1;
 
// set number of records per page
$records_per_page = 5;
 
// calculate for the query LIMIT clause
$from_record_num = ($records_per_page * $page) - $records_per_page;
 
// retrieve records here
// include database and object files
include_once 'config/database.php';
include_once 'objects/learn.php';
 
// instantiate database and objects
$database = new Database();
$db = $database->getConnection();
 
$learn = new Learn($db);
 
// query learn
$stmt = $learn->readAll($from_record_num, $records_per_page);

$num = $stmt->rowCount();

// set page header
$page_title = "Read learning";
include_once "header.php";
 
// contents will be here
echo "<div class='right-button-margin'>
    <a href='add_learning.php' class='btn btn-default pull-right'>Add learning</a>
</div>";

// display the products if there are any

// display the learning if there are any
if($num>0){
 
    echo "<table class='table table-hover table-responsive table-bordered'>";
        echo "<tr>";
            echo "<th>Title</th>";
            echo "<th>Time spent</th>";
            echo "<th>Learning</th>";
            echo "<th>Resources</th>";
            echo "<th>Created on</th>";
            echo "<th>Actions</th>";
        echo "</tr>";
 
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)){
 
            extract($row);
 
            echo "<tr>";
                echo "<td>{$title}</td>";
                echo "<td>{$time_spent}</td>";
                echo "<td>{$learning}</td>";
                echo "<td>{$resources}</td>";
                echo "<td>{$created}</td>";
                echo "<td>";
                
                // read one, edit and delete button will be here
				echo "<a href='read_one.php?id={$id}' class='btn btn-primary left-margin'>
				    <span class='glyphicon glyphicon-list'></span> Read
				</a>
				 
				<a href='update_learning.php?id={$id}' class='btn btn-info left-margin'>
				    <span class='glyphicon glyphicon-edit'></span> Edit
				</a>
				 
				<a delete-id='{$id}' class='btn btn-danger delete-object'>
				    <span class='glyphicon glyphicon-remove'></span> Delete
				</a>";
                echo "</td>";
 
            echo "</tr>";
 
        }
 
    echo "</table>";
 
    // paging buttons will be here
	    // the page where this paging is used
	$page_url = "index.php?";
	 
	// count all learning in the database to calculate total pages
	$total_rows = $learn->countAll();
	 
	// paging buttons here
	include_once 'paging.php';
}
 
// tell the user there are no learnings
else{
    echo "<div class='alert alert-info'>No learning found.</div>";
}
 
// set page footer
include_once "footer.php";
?>