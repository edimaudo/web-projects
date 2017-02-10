/*
Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
*/

function spinalCase(str) {
  var newstr = "";
  for (var i = 0; i <str.length; i++) {
    if (str[i].toUpperCase() === str[i]) {
       newstr += "-" + str[i].toLowerCase();
    } else {
      newstr += str[i];
    }
  }
  if (newstr[0] !== "-"){
    return newstr;
  } else {
    return str.replace(/[\W_]/ig,"-").toLowerCase();
  }
}