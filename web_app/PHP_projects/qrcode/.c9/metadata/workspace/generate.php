{"filter":false,"title":"generate.php","tooltip":"/generate.php","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["b"],"id":73}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"remove","lines":["b"],"id":74},{"start":{"row":2,"column":5},"end":{"row":4,"column":11},"action":"insert","lines":["body>","        ","    </body>"]}],[{"start":{"row":7,"column":0},"end":{"row":20,"column":1},"action":"remove","lines":["<?php ","if(isset($_POST['generate_text']))","{"," include('phpqrcode/qrlib.php'); "," $text=$_POST['qr_text'];"," $folder=\"images/\";"," $file_name=\"qr.png\";"," $file_name=$folder.$file_name;"," QRcode::png($text,$file_name);"," echo\"<img\".\"id='info'\".\"src='images/qr.png '>\";"," "," //To Display Code Without Storing"," QRcode::png($text);","}"],"id":75}],[{"start":{"row":3,"column":7},"end":{"row":16,"column":1},"action":"insert","lines":["<?php ","if(isset($_POST['generate_text']))","{"," include('phpqrcode/qrlib.php'); "," $text=$_POST['qr_text'];"," $folder=\"images/\";"," $file_name=\"qr.png\";"," $file_name=$folder.$file_name;"," QRcode::png($text,$file_name);"," echo\"<img\".\"id='info'\".\"src='images/qr.png '>\";"," "," //To Display Code Without Storing"," QRcode::png($text);","}"],"id":76}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":2},"action":"remove","lines":["?>"],"id":77}],[{"start":{"row":16,"column":2},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":78}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["?>"],"id":79}],[{"start":{"row":1,"column":6},"end":{"row":2,"column":4},"action":"insert","lines":["","    "],"id":80}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["<"],"id":81}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["h"],"id":82}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["e"],"id":83}],[{"start":{"row":2,"column":7},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":84},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "],"id":85}],[{"start":{"row":2,"column":7},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":86}],[{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["a"],"id":87}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":8},"action":"remove","lines":["hea"],"id":88},{"start":{"row":2,"column":5},"end":{"row":4,"column":11},"action":"insert","lines":["head>","        ","    </head>"]}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["<"],"id":89}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["s"],"id":90}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["t"],"id":91}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":11},"action":"remove","lines":["st"],"id":92},{"start":{"row":3,"column":9},"end":{"row":5,"column":16},"action":"insert","lines":["style type=\"text/css\">","            ","        </style>"]}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["i"],"id":93}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["n"],"id":94}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["f"],"id":95}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["o"],"id":96}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["#"],"id":97}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["{"],"id":98}],[{"start":{"row":4,"column":18},"end":{"row":6,"column":13},"action":"insert","lines":["","                ","            }"],"id":99}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["w"],"id":100}],[{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["i"],"id":101}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["d"],"id":102}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["t"],"id":103}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["h"],"id":104}],[{"start":{"row":5,"column":21},"end":{"row":5,"column":23},"action":"insert","lines":[":;"],"id":105}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["3"],"id":106}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["0"],"id":107}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["0"],"id":108}],[{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":["p"],"id":109}],[{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["x"],"id":110}],[{"start":{"row":5,"column":28},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":111},{"start":{"row":6,"column":0},"end":{"row":6,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["e"],"id":112}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["e"],"id":113}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["h"],"id":114}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["e"],"id":115}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["i"],"id":116}],[{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["g"],"id":117}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["h"],"id":118}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["t"],"id":119}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":24},"action":"insert","lines":[":;"],"id":120}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["3"],"id":121}],[{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["0"],"id":122}],[{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["0"],"id":123}],[{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["p"],"id":124}],[{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["x"],"id":125}],[{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"remove","lines":["s"],"id":126}],[{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"remove","lines":["s"],"id":127}],[{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"remove","lines":["c"],"id":128}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"remove","lines":["/"],"id":129}],[{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"remove","lines":["t"],"id":130}],[{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"remove","lines":["x"],"id":131}],[{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"remove","lines":["e"],"id":132}],[{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":["t"],"id":133}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":22},"action":"remove","lines":["\"\""],"id":134}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"remove","lines":["="],"id":135}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"remove","lines":["e"],"id":136}],[{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":["p"],"id":137}],[{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"remove","lines":["y"],"id":138}],[{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":["t"],"id":139}],[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":[" "],"id":140}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":23},"action":"remove","lines":["\"id='info'\""],"id":141}],[{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"remove","lines":["."],"id":142}],[{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"remove","lines":["\""],"id":143}],[{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"remove","lines":["."],"id":144}],[{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"remove","lines":["\""],"id":145}],[{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":[" "],"id":146}],[{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["\""],"id":147}],[{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":["."],"id":148}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":14},"action":"insert","lines":["\"\""],"id":149}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["."],"id":150}],[{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["\""],"id":151}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["i"],"id":152}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["d"],"id":153}],[{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["="],"id":154}],[{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["'"],"id":155}],[{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["'"],"id":156}],[{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["i"],"id":157}],[{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["n"],"id":158}],[{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["f"],"id":159}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":["o"],"id":160}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":22},"action":"remove","lines":["id='info'"],"id":161}],[{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"remove","lines":[" "],"id":162}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["."],"id":163}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":15},"action":"remove","lines":["\"\""],"id":164}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":["\""],"id":165}],[{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"remove","lines":["."],"id":166}],[{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"remove","lines":["\""],"id":167}],[{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":[" "],"id":168}],[{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["\""],"id":169}],[{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":["."],"id":170}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["\""],"id":171}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":[" "],"id":172}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":23},"action":"insert","lines":["id='info'"],"id":173}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":24},"end":{"row":20,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1489026369000,"hash":"b0f79876573987e5d54a69cf1ae4c3412e7c1d37"}