/*
Return true if the given string is a palindrome. Otherwise, return false.
*/

function palindrome(str) {

  str=str.replace(/[\W_]/g, '').toLowerCase();
  var removeChar = str.split('').reverse().join('');
  return str == removeChar;
}
