{"filter":false,"title":"process.php","tooltip":"/process.php","undoManager":{"mark":34,"position":34,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["<"],"id":1}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["h"],"id":2}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["t"],"id":3}],[{"start":{"row":0,"column":3},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":0,"column":3},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["t"],"id":6}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["h"],"id":7}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["<"],"id":8}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":5},"action":"insert","lines":["<?php"],"id":9}],[{"start":{"row":0,"column":5},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["?"],"id":12}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":[">"],"id":13}],[{"start":{"row":1,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["if( isset($_POST) ){","     ","    //form validation vars","    $formok = true;","    $errors = array();","     ","    //sumbission data","    $ipaddress = $_SERVER['REMOTE_ADDR'];","    $date = date('d/m/Y');","    $time = date('H:i:s');","     ","    //form data","    $name = $_POST['name'];    ","    $email = $_POST['email'];","    $telephone = $_POST['telephone'];","    $enquiry = $_POST['enquiry'];","    $message = $_POST['message'];","     ","    //form validation to go here....","     ","}"],"id":14}],[{"start":{"row":21,"column":1},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":15}],[{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":16}],[{"start":{"row":23,"column":0},"end":{"row":27,"column":1},"action":"insert","lines":["//validate name is not empty","if(empty($name)){","    $formok = false;","    $errors[] = \"You have not entered a name\";","}"],"id":17}],[{"start":{"row":27,"column":1},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":18}],[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":19}],[{"start":{"row":29,"column":0},"end":{"row":37,"column":1},"action":"insert","lines":["//validate email address is not empty","if(empty($email)){","    $formok = false;","    $errors[] = \"You have not entered an email address\";","//validate email address is valid","}elseif(!filter_var($email, FILTER_VALIDATE_EMAIL)){","    $formok = false;","    $errors[] = \"You have not entered a valid email address\";","}"],"id":20}],[{"start":{"row":37,"column":1},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":21}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":22}],[{"start":{"row":39,"column":0},"end":{"row":48,"column":1},"action":"insert","lines":["//validate message is not empty","if(empty($message)){","    $formok = false;","    $errors[] = \"You have not entered a message\";","}","//validate message is greater than 20 charcters","elseif(strlen($message) < 20){","    $formok = false;","    $errors[] = \"Your message must be greater than 20 characters\";","}"],"id":23}],[{"start":{"row":48,"column":1},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":24}],[{"start":{"row":49,"column":0},"end":{"row":50,"column":0},"action":"insert","lines":["",""],"id":25}],[{"start":{"row":50,"column":0},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":26}],[{"start":{"row":51,"column":0},"end":{"row":65,"column":1},"action":"insert","lines":["if($formok){","    $headers = \"From: info@example.com\" . \"\\r\\n\";","    $headers .= 'Content-type: text/html; charset=iso-8859-1' . \"\\r\\n\";","     ","    $emailbody = \"<p>You have recieved a new message from the enquiries form on your website.</p>","                  <p><strong>Name: </strong> {$name} </p>","                  <p><strong>Email Address: </strong> {$email} </p>","                  <p><strong>Telephone: </strong> {$telephone} </p>","                  <p><strong>Enquiry: </strong> {$enquiry} </p>","                  <p><strong>Message: </strong> {$message} </p>","                  <p>This message was sent from the IP Address: {$ipaddress} on {$date} at {$time}</p>\";","     ","    mail(\"enquiries@example.com\",\"New Enquiry\",$emailbody,$headers);","     ","}"],"id":27}],[{"start":{"row":65,"column":1},"end":{"row":66,"column":0},"action":"insert","lines":["",""],"id":28}],[{"start":{"row":66,"column":0},"end":{"row":67,"column":0},"action":"insert","lines":["",""],"id":29}],[{"start":{"row":67,"column":0},"end":{"row":79,"column":6},"action":"insert","lines":[" //what we need to return back to our form","    $returndata = array(","        'posted_form_data' => array(","            'name' => $name,","            'email' => $email,","            'telephone' => $telephone,","            'enquiry' => $enquiry,","            'message' => $message","        ),","        'form_ok' => $formok,","        'errors' => $errors","    );","      "],"id":30}],[{"start":{"row":79,"column":5},"end":{"row":79,"column":6},"action":"remove","lines":[" "],"id":31}],[{"start":{"row":79,"column":4},"end":{"row":79,"column":5},"action":"remove","lines":[" "],"id":32}],[{"start":{"row":79,"column":4},"end":{"row":80,"column":0},"action":"insert","lines":["",""],"id":33},{"start":{"row":80,"column":0},"end":{"row":80,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":80,"column":0},"end":{"row":80,"column":4},"action":"remove","lines":["    "],"id":34}],[{"start":{"row":80,"column":0},"end":{"row":88,"column":5},"action":"insert","lines":["    //if this is not an ajax request","    if(empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) !== 'xmlhttprequest'){","        //set session variables","        session_start();","        $_SESSION['cf_returndata'] = $returndata;","         ","        //redirect back to form","        header('location: ' . $_SERVER['HTTP_REFERER']);","    }"],"id":35}]]},"ace":{"folds":[],"scrolltop":382.5,"scrollleft":0,"selection":{"start":{"row":88,"column":5},"end":{"row":88,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":22,"state":"php-start","mode":"ace/mode/php"}},"timestamp":1488939943000,"hash":"4423949128b605e5738d19bb51ac00f597de9708"}