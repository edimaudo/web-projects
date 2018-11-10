<?php

function alexaRank($url) {
 $alexaData = simplexml_load_file("http://data.alexa.com/data?cli=10&url=".$url);
 $alexa['globalRank'] =  isset($alexaData->SD->POPULARITY) ? $alexaData->SD->POPULARITY->attributes()->TEXT : 0 ;
 $alexa['CountryRank'] =  isset($alexaData->SD->COUNTRY) ? $alexaData->SD->COUNTRY->attributes() : 0 ;
 return json_decode(json_encode($alexa), TRUE);
}



if(isset($_POST['submit_url'])){
 $url = $_POST['url'];
 $alexaglobalRank = "none";
 $alexacountryName = "none";
 $alexacountryRank = "none";
 $url_headers = @get_headers($url);
 if(strpos($url_headers[0],'200')){
     $exist = "URL Exist";
     $urlother = $_GET['siteinfo'];
     $alexa = alexaRank($urlother);
     $alexaglobalRank = $alexa['globalRank'][0];
     $alexacountryName = $alexa['CountryRank']['@attributes']['NAME'];
     $alexacountryRank = $alexa['CountryRank']['@attributes']['RANK'];

 } else {
        $exist = "URL Does Not Exist";
 }

   $arr = array("url"=> $url, 
   "url_exist" => $exist, 
   "alexa_global_rank" => $alexaglobalRank, 
   "alexa_country_name" =>  $alexacountryName, 
   "alexa_country_rank" =>  $alexacountryRank); 
   echo json_encode($arr);
}




?>