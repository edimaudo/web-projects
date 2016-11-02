/*
Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a multidimensional array.
*/

function chunk(arr, size) {
  var tempArray = [];
  var arrayLength = arr.length;
  var i = 0;
  while (i < arrayLength){
    tempArray.push(arr.slice(i,i+size));
    i= i + size;
  }
    
  
  return tempArray;
}