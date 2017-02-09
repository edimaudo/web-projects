/*
Caesars Cipher
Write a function which takes a ROT13 encoded string as input and returns a decoded string.
*/

function rot13(str) { // LBH QVQ VG!
  var letter = "";
  var translate = "";
  
  for (var i = 0; i < str.length; i++){
    letter = str[i];
    var position = 0;
    position = letter.charCodeAt();
    //alert(position);
    
    if (letter.match("[,!@#$%^&*()?.' ']")){
    	translate+=letter;
    } else {
    	if (position > 77){
      	translate += String.fromCharCode(position-13);
      } else {
      	translate += String.fromCharCode(position+13);
      }
    	
    }
    
  }
  return translate;
}


// Change the inputs below to test
rot13("SERR PBQR PNZC");

