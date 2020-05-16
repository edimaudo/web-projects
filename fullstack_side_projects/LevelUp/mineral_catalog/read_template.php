<?php
// search form
echo "<form role='search' action='search.php'>";
    echo "<div class='input-group col-md-3 pull-left margin-right-1em'>";
        $search_value=isset($search_term) ? "value='{$search_term}'" : "";
        echo "<input type='text' class='form-control' placeholder='Type mineral information..' name='s' id='srch-term' required {$search_value} />";
        echo "<div class='input-group-btn'>";
            echo "<button class='btn btn-primary' type='submit'><i class='glyphicon glyphicon-search'></i></button>";
        echo "</div>";
    echo "</div>";
echo "</form>";
 

echo "<div class="grid-100">";
    echo "<ul class="minerals__container">"; 
// display the minerals if there are any
if($total_rows>0){
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)){
            extract($row);
                echo "<li class="minerals__item">"
                    echo "<a class="minerals__anchor" href="detail.html">{$title}</a>";
                echo "</li>";
        }

}
 
// tell the user there are no minerals
else{
    echo "<div class='alert alert-danger'>No Minerals found.</div>";
}

       echo "</ul>"    
    echo "</div>"

?>