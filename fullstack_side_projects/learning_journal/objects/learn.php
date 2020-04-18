<?php
    class Learn{
     
            // database connection and table name
            private $conn;
            private $table_name = "learn";
         
            // object properties
            public $id;
            public $title;
            public $created;
            public $time_spent;
            public $learning;
            public $resources;
     
            public function __construct($db){
                $this->conn = $db;
            }
     
            // create learning
            function create(){
         
                    //write query
                    $query = "INSERT INTO
                                " . $this->table_name . "
                            SET
                                title=:title, created=:created, time_spent=:time_spent, learning=:learning, resources=:resources" ;
         
                    $stmt = $this->conn->prepare($query);
         
                    // posted values
                    $this->title=htmlspecialchars(strip_tags($this->title));
                    $this->time_spent=htmlspecialchars(strip_tags($this->time_spent));
                    $this->learning=htmlspecialchars(strip_tags($this->learning));
                    $this->resources=htmlspecialchars(strip_tags($this->resources));
                    $this->created = date('Y-m-d H:i:s');// to get date 'created' field
             
                    // bind values 
                    $stmt->bindParam(":title", $this->title);
                    $stmt->bindParam(":time_spent", $this->time_spent);
                    $stmt->bindParam(":learning", $this->learning);
                    $stmt->bindParam(":resources", $this->resources);
                    $stmt->bindParam(":created", $this->created);
         
                if($stmt->execute()){
                    return true;
                }else{
                    return false;
                }
         
            }

/*            function readAll(){
             
                $query = "SELECT
                            id, title, time_spent, learning, resources
                        FROM
                            " . $this->table_name . "
                        ORDER BY
                            title ASC";
                        //LIMIT
                        //    {$from_record_num}, {$records_per_page}
             
                $stmt = $this->conn->prepare( $query );
                $stmt->execute();
             
                return $stmt;
            }*/

            function readAll($from_record_num, $records_per_page){
             
                $query = "SELECT
                            id, title, time_spent, learning, resources, created
                        FROM
                            " . $this->table_name . "
                        ORDER BY
                            created DESC
                        LIMIT
                           {$from_record_num}, {$records_per_page}";
             
                $stmt = $this->conn->prepare( $query );
                $stmt->execute();
             
                return $stmt;
            }

            // used for paging learning
            public function countAll(){
             
                $query = "SELECT id FROM " . $this->table_name . "";
             
                $stmt = $this->conn->prepare( $query );
                $stmt->execute();
             
                $num = $stmt->rowCount();
             
                return $num;
            }

    }
?>