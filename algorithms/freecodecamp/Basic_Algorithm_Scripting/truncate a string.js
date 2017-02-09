/*
Truncate a string (first argument) if it is longer than the given maximum string length (second argument). Return the truncated string with a "..." ending.

Note that the three dots at the end add to the string length.
*/

function truncateString(str, num) {
  if (num <= 3){
    return str.slice(0,num) + "...";
  }
  return str.length <= num? str: str.slice(0,num-3) + "...";
}

truncateString("A-tisket a-tasket A green and yellow basket", 11);
