<?php
session_start();

$id = $_SESSION ["id"];
$firstName = $_SESSION ["firstName"];
$lastName = $_SESSION ["lastName"];
$category = $_SESSION ["category"];

?>

<html>
    <head>
        <title>Composer Information</title>

        <link rel="stylesheet" type="text/css" href="stylesheet.css">
    </head>
    <body>

        <table>
            <tr>
                <th colspan="2">Composer Information</th>
            </tr>
            <tr>
                <td>First Name: </td>
                <td><?php echo $firstName; ?></td>
            </tr>
            <tr>
                <td>Last Name: </td>
                <td><?php echo $lastName; ?></td>
            </tr>
            <tr>
                <td>ID: </td>
                <td><?php echo $id; ?></td>
            </tr>
            <tr>
                <td>Category: </td>
                <td><?php echo $category; ?></td>
            </tr>
        </table>

        <p>Go back to <a href="index.html" class="link">application home</a>.</p>
    </body>
</html>