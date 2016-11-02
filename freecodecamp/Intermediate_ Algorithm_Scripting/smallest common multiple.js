/*
Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

The range will be an array of two numbers that will not necessarily be in numerical order.
*/

function smallestCommons(arr) {
  var tempArray = [];
  if (arr[0] < arr[1]) {
    for (var i = arr[0]; i <= arr[1]; i++) {
      tempArray.push(i);
    }
  } else {
    for (var i = arr[0]; i >= arr[1]; i--) {
      tempArray.push(i);
    }
  }

  function gcd(a, b) {
    return !b ? a : gcd(b, a % b);
  }

  function lcm(a, b) {
    return (a * b) / gcd(a, b);
  }

  var multiple = arr[0];
  tempArray.forEach(function(n) {
    multiple = lcm(multiple, n);
  });

  return multiple;
}

console.log(smallestCommons([1, 5]));