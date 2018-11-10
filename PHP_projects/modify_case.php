<?php

// define a function

function changeCase($str, $flag) {

    /* check the flag variable and branch the code */

    switch($flag) {

        case 'U':

            print strtoupper($str)."<br />";

            break;

        case 'L':

            print strtolower($str)."<br />";

            break;

        default:

            print $str."<br />";

            break;

    }

}

// call the function

changeCase("The cow jumped over the moon", "U");

changeCase("Hello Sam", "L");

?>