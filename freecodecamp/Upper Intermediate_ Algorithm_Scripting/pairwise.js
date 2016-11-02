/*
Return the sum of all indices of elements of 'arr' that can be paired with one other element to form a sum that equals the value in the second argument 'arg'. If multiple sums are possible, return the smallest sum. Once an element has been used, it cannot be reused to pair with another.
*/

function pairwise(arr, arg) {
  var tempArray = [];

  for (var i = 0; i < arr.length; i++) {
    for (var j = 0; j < arr.length; j++) {
      if (i !== j && arr[i] + arr[j] === arg) {
        tempArray.push(j);
      }
    }
  }
  uniqueArray = tempArray.filter(function(item, pos) {
    return tempArray.indexOf(item) == pos;
  })
  uniqueArray.sort();

  return uniqueArray.length !== tempArray.length ?
   uniqueArray.slice(0, uniqueArray.length - 1).reduce(add, 0): uniqueArray.reduce(add, 0);
}

function add(a, b) {
  return a + b;
}