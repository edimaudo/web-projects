/*
Repeat a given string (first argument) n times (second argument). Return an empty string if n is a negative number.
*/

function repeat(str, num) {
  return num < 0 ? "":Array(num+1).join(str);
}