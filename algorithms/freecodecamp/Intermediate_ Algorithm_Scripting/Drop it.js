/*
Drop the elements of an array (first argument), starting from the front, until the predicate (second argument) returns true.
*/
function drop(arr, func) {
  var newarr = arr.filter(func);
  beginposition = arr.indexOf(newarr[0]);
  return newarr.length < 1 ? []:arr.slice(beginposition, arr.length);
}