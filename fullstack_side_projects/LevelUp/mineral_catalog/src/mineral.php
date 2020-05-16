<?php
    class Mineral{
// database connection and table name
            private $conn;
            private $table_name = "minerla";
         
            // object properties
            public $id;
            public $title;

            public function __construct($db){
                $this->conn = $db;
            }

            function readAll(){
             
                $query = "SELECT
                            id, title
                        FROM
                            " . $this->table_name . "
                        ORDER BY
                            created DESC";
             
                $stmt = $this->conn->prepare( $query );
                $stmt->execute();
             
                return $stmt;
            }

            public function countAll(){
             
                $query = "SELECT id FROM " . $this->table_name . "";
             
                $stmt = $this->conn->prepare( $query );
                $stmt->execute();
             
                $num = $stmt->rowCount();
             
                return $num;
            }

             function readOne(){
 
                $query = "SELECT
                            title, id
                        FROM
                            " . $this->table_name . "
                        WHERE
                            id = ?
                        LIMIT
                            0,1";
             
                $stmt = $this->conn->prepare( $query );
                $stmt->bindParam(1, $this->id);
                $stmt->execute();
             
                $row = $stmt->fetch(PDO::FETCH_ASSOC);
             
                $this->id = $row['id'];
                $this->title = $row['title'];
            }

           //search information -- update the code for later
            public function search($search_term, $from_record_num, $records_per_page){
             
                // select query
                $query = "SELECT
                            p.id, p.title, p.time_spent, p.learning, p.resources, p.created
                        FROM
                            " . $this->table_name . " p
                        WHERE
                            p.title LIKE ? OR p.learning LIKE ?
                        ORDER BY
                            p.title ASC
                        LIMIT
                            ?, ?";
             
                // prepare query statement
                $stmt = $this->conn->prepare( $query );
             
                // bind variable values
                $search_term = "%{$search_term}%";
                $stmt->bindParam(1, $search_term);
                $stmt->bindParam(2, $search_term);
                $stmt->bindParam(3, $from_record_num, PDO::PARAM_INT);
                $stmt->bindParam(4, $records_per_page, PDO::PARAM_INT);
             
                // execute query
                $stmt->execute();
             
                // return values from database
                return $stmt;
            }
             
            public function countAll_BySearch($search_term){
             
                // select query
                $query = "SELECT
                            COUNT(*) as total_rows
                        FROM
                            " . $this->table_name . " p 
                        WHERE
                            p.title LIKE ? OR p.learning LIKE ?";
             
                // prepare query statement
                $stmt = $this->conn->prepare( $query );
             
                // bind variable values
                $search_term = "%{$search_term}%";
                $stmt->bindParam(1, $search_term);
                $stmt->bindParam(2, $search_term);
             
                $stmt->execute();
                $row = $stmt->fetch(PDO::FETCH_ASSOC);
             
                return $row['total_rows'];
            }





    }

?>