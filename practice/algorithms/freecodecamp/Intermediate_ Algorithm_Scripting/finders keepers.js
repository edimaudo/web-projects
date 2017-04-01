/*
Create a function that looks through an array (first argument) and returns the first element in the array that passes a truth test (second argument).
*/

function find(arr, func) {
  var output = arr.filter(func);
  return output[0];
}