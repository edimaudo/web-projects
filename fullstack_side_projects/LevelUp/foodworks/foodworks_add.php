<?php
// include database and object files
include_once 'config/database.php';
include_once 'src/foodworks.php';
 
// get database connection
$database = new Database();
$db = $database->getConnection();
 
// pass connection to objects
$foodworks = new Foodworks($db);
// set page headers

$page_title = "Add Product";
include_once "header.php";
 
// contents will be here
echo "<div class='right-button-margin'>";
    echo "<a href='index.php' class='btn btn-default pull-right'>Read Product</a>";
echo "</div>";
 
?>
<!-- PHP post code will be here -->
<?php 
// if the form was submitted
if($_POST){
 
    // set product property values
    $foodworks->title = $_POST['title'];
    $foodworks->price = $_POST['price'];
    $foodworks->description = $_POST['description'];
    $foodworks->image_url = $_POST['image_url'];
 
    // create the product
    if($foodworks->create()){
        echo "<div class='alert alert-success'>Product was added.</div>";
    }
 
    // if unable to create the product, tell the user
    else{
        echo "<div class='alert alert-danger'>Unable to add Product.</div>";
    }
}
?>
 
<!-- HTML form for creating a product -->
<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">
 
    <table class='table table-hover table-responsive table-bordered'>
 
        <tr>
            <td>Title</td>
            <td><input type='text' name='title' class='form-control' /></td>
        </tr>
 
        <tr>
            <td>Price</td>
            <td><input type='text' name='price' class='form-control' /></td>
        </tr>
 
        <tr>
            <td>description</td>
            <td><textarea name='description' class='form-control'></textarea></td>
        </tr>
 
        <tr>
            <td>image_url</td>
				<td><input type='text' name='image_url' class='form-control' /></td>
        </tr>
 
        <tr>
            <td></td>
            <td>
                <button type="submit" class="btn btn-primary">Create</button>
            </td>
        </tr>
 
    </table>
</form>
<?php 
// footer
include_once "footer.php";
?>