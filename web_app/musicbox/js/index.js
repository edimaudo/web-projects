// design a music box where each box produces a different sound

/*
- get or create the sounds 
- embed the right html tags
- build different boxes 
- when the box is clicked it should produce a sound
  - might have to use a function here
*/

$(document).ready(function(){
  var anote = document.getElementById("aaudio");
  var bnote = document.getElementById("baudio");
  var cnote = document.getElementById("caudio");  
  var dnote = document.getElementById("daudio");
  var enote = document.getElementById("eaudio");
  var fnote = document.getElementById("faudio");
  var gnote = document.getElementById("gaudio");
 
  $('#a').mousedown(function(){
    anote.currentTime = 0;
    anote.play();
  });
  
  $('#b').mousedown(function(){
    bnote.currentTime = 0;
    bnote.play();
  });  
 
  $('#c').mousedown(function(){
    cnote.currentTime = 0;
    cnote.play();
  });
 
  $('#d').mousedown(function(){
    dnote.currentTime = 0;
    dnote.play();
  });  
  
  $('#e').mousedown(function(){
    enote.currentTime = 0;
    enote.play();
  });
  
  $('#f').mousedown(function(){
    fnote.currentTime = 0;
    fnote.play();
  });
  
  $('#g').mousedown(function(){
    gnote.currentTime = 0;
    gnote.play();
  });  

});