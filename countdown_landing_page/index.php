<?php
  if(inset($_POST['submit'])){
    $from = $_POST['email'];
    $to = "edimaudo@gmail.com";
    $subject = "Email signup";
    $body = "Please sign me up for the mailing list";

    if (!$_POST['email']){
      $emailError = "<div class="text-danger">Please enter a valid email address</div>";
    }

    if(!$emailError){
        if(mail($to,$subject,$from)){
          $result = "<div class="text-success">thank you we will keep you updated</div>";
        } else {
          $result = "Sorry there has been an error please try again";
        }
    }
  }
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags always come first -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" type="text/css" href="font-awesome/css/font-awesome.css">
    <link href="https://fonts.googleapis.com/css?family=Just+Another+Hand" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.4/css/bootstrap.min.css" integrity="2hfp1SzUoho7/TsGGGDaFdsuuDL0LX2hnUp6VkX3CUQ2K4K+xjboZdsXyp4oUHZj" crossorigin="anonymous">
  </head>
  <body>

  <section id="logo">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <img src="img/my-logo.png" class="img-fluid"/>
        </div>
      </div>
    </div>
  </section>

  <section id="intro">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <p>Going to launch very soon</p>
        </div>
      </div>
    </div>
  </section>

    <section id="counter">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="countdown"></div>
        </div>
      </div>
    </div>
  </section>

  <section id="icons">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <ul class="list-inline">
            <a href="https://twitter.com/edimaudo" target="blank"><li class="list-inline-item"><i class="fa fa-twitter-square fa-3x twitter" aria-hidden="true"></i></li></a>
            <a href="https://www.facebook.com/esudo" target="blank"><li class="list-inline-item"><i class="fa fa-facebook-square fa-3x facebook" aria-hidden="true"></i></li></a>
            <a href="https://plus.google.com/101745668770194581889" target="blank"><li class="list-inline-item"><i class="fa fa-google-plus-square fa-3x google" aria-hidden="true"></i></li></a>
            <a href="https://www.instagram.com/edimaudo/" target="blank"><li class="list-inline-item"><i class="fa fa-instagram fa-3x instagram" aria-hidden="true"></i></li></a>                                    
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section id="signup">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <form class="form-inline" role="form" method="post" action="#signup">
            <input type="email" class ="form-control form-control-sn" name="email" placeholder="enter your email"/>
            <button type="submit" class="btn btn-signup btn-sn" name="submit" value="send" >find out more</button>
          </form>
          <?php echo $emailError;?>
          <?php echo $result;?>
        </div>
      </div>
    </div>
  </section>

    <!-- jQuery first, then Tether, then Bootstrap JS. -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.0.0/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.2.0/js/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.4/js/bootstrap.min.js" integrity="VjEeINv9OSwtWFLAtmc4JCtEJXXBub00gtSnszmspDLCtC0I4z4nqz7rEFbIZLLU" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script type="text/javascript" src="js/jquery.countdown.js"></script>
<script>
  $(function() {
    $('.countdown').countdown({
        date: "June 7, 2017 15:03:26"
    });
});
</script>
  </body>
</html>