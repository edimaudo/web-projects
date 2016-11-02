/*
Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.

For the purpose of this exercise, you should also capitalize connecting words like "the" and "of".
*/

function titleCase(str) {
  str = str.toLowerCase();
  var strval = "";
  var beginVal = str.charAt(0).toUpperCase();
  for (var i = 1; i<str.length;i++){
    if (str.charAt(i-1) === " ") {
      strval = strval + str.charAt(i).toUpperCase();
    } else {
        strval = strval + str.charAt(i);
    }
  }
  return beginVal + strval;
}