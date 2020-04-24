<?php
// retrieve one genre will be here
// get ID of the genre to be edited
$id = isset($_GET['id']) ? $_GET['id'] : die('ERROR: missing ID.');
 
// include database and object files
include_once 'config/database.php';
include_once 'objects/movie.php';

 
// get database connection
$database = new Database();
$db = $database->getConnection();
 
// prepare objects
$movie = new Movie($db);
 
// set ID property of genre to be edited
$movie->id = $id;
 
// read the details of movie to be edited
$movie->readOne();

// set page header
$page_title = "Update movie";
include_once "header.php";


// contents will be here
echo "<div class='right-button-margin'>";
    echo "<a href='index.php' class='btn btn-default pull-right'>Movies</a>";
echo "</div>";
?>


<!-- 'update movie' form will be here -->

<!-- post code will be here -->
<?php 
// if the form was submitted
if($_POST){
 
    // set movie property values
    $movie->title = $_POST['title'];
    $movie->release_date = $_POST['release_date'];
    $movie->genre = $_POST['genre'];
    $movie->price = $_POST['price'];
 
    // update the movie
    if($movie->update()){
        echo "<div class='alert alert-success alert-dismissable'>";
            echo "movie was updated.";
        echo "</div>";
    }
 
    // if unable to update the movie, tell the user
    else{
        echo "<div class='alert alert-danger alert-dismissable'>";
            echo "Unable to update movie.";
        echo "</div>";
    }
}
?>

 
<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"] . "?id={$id}");?>" method="post">
    <table class='table table-hover table-responsive table-bordered'>
 
        <tr>
            <td>Title</td>
            <td><input type='text' name='title' value='<?php echo $movie->title; ?>' class='form-control' required/></td>
        </tr>
 
        <tr>
            <td>Release Date</td>
            <td><input type='date' name='release_date' value='<?php echo $movie->release_date; ?>' class='form-control' /></td>
        </tr>
 
        <tr>
            <td>Genre</td>
            <td><input type="text" name='genre' value='<?php echo $movie->genre; ?>'class='form-control'/> </td>
        </tr>
 
        <tr>
            <td>Price</td>
            <td><input type="number" name='price' value='<?php echo $movie->price; ?>'class='form-control'/> </td>
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