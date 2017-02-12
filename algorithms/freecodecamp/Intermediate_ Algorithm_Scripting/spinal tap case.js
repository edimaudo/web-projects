/*
Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
*/

function spinalCase(str) {
  // "It's such a fine line between stupid, and clever."
  // --David St. Hubbins
  str = str.replace(/([^[A-Za-z-])|\w([A-Z])/g, function (match, offset, string) {
      if (string === undefined){
      return '-';
     } else {return match.substr(offset,1)+ '-' + string;}
  }).toLowerCase();
  return str;
}