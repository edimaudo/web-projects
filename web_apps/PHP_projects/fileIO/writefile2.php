<?php

// set file to write
$filename = '/tmp/dump.txt';

// write to file

file_put_contents($filename, "Look, Ma, I wrote a file!
") or die('Could not write to file');

?>