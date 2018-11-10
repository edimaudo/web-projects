<?php

// set file to write
$file = '/tmp/dump.txt';

// open file

$fh = fopen($file, 'w') or die('Could not open file!');

// write to file

fwrite($fh, "Look, Ma, I wrote a file!
") or die('Could not write to file');

// close file

fclose($fh);

?>