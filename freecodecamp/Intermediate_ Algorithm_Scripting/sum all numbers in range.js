/*
We'll pass you an array of two numbers. Return the sum of those two numbers and all numbers between them.

The lowest number will not always come first.
*/
function sumAll(arr) {
  sumval = 0;
  if (arr[0] < arr[1]){
    for (var i = arr[0]; i <= arr[1]; i++){
      sumval += i;  
    }
  } else {
    for (var i = arr[1]; i <= arr[0]; i++){
      sumval += i;  
    }    
  }
  return sumval;
}