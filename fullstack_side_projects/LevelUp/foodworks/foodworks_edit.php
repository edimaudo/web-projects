<?php
// retrieve one foodworksing will be here
// get ID of the foodworksing to be edited
$id = isset($_GET['id']) ? $_GET['id'] : die('ERROR: missing ID.');
 
// include database and object files
include_once 'config/database.php';
include_once 'src/foodworks.php';

 
// get database connection
$database = new Database();
$db = $database->getConnection();
 
// prepare objects
$foodworks = new Foodworks($db);
 
// set ID property of product to be edited
$foodworks->id = $id;
 
// read the details of product to be edited
$foodworks->readOne();

// set page header
$page_title = "Update Product";
include_once "header.php";


// contents will be here
echo "<div class='right-button-margin'>";
    echo "<a href='index.php' class='btn btn-default pull-right'>Read Products</a>";
echo "</div>";
?>


<!-- 'update Product' form will be here -->

<!-- post code will be here -->
<?php 
// if the form was submitted
if($_POST){
 
    // set foodworks property values
    $foodworks->title = $_POST['title'];
    $foodworks->price = $_POST['price'];
    $foodworks->description = $_POST['description'];
    $foodworks->image_url = $_POST['image_url'];
 
    // update the product
    if($foodworks->update()){
        echo "<div class='alert alert-success alert-dismissable'>";
            echo "Product was updated.";
        echo "</div>";
    }
 
    // if unable to update the product, tell the user
    else{
        echo "<div class='alert alert-danger alert-dismissable'>";
            echo "Unable to update Product";
        echo "</div>";
    }
}
?>

 
<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"] . "?id={$id}");?>" method="post">
    <table class='table table-hover table-responsive table-bordered'>
 
        <tr>
            <td>Title</td>
            <td><input type='text' name='title' value='<?php echo $foodworks->title; ?>' class='form-control' /></td>
        </tr>
 
        <tr>
            <td>Price</td>
            <td>$<input type='text' name='price' value='<?php echo $foodworks->price; ?>' class='form-control' /></td>
        </tr>
 
        <tr>
            <td>description</td>
            <td><textarea name='description' class='form-control'><?php echo $foodworks->description; ?></textarea></td>
        </tr>
 
        <tr>
            <td>Image</td>
            <td>$<input type='text' name='image_url' value='<?php echo $foodworks->image_url; ?>' class='form-control' /></td>>
        </tr>
 
        <tr>
            <td></td>
            <td>
                <button type="submit" class="btn btn-primary">Update</button>
            </td>
        </tr>
 
    </table>
</form>

<?php 

 

 
// set page footer
include_once "footer.php";
?>