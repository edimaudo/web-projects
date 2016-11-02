//Bonfire: Return Largest Numbers in Arrays

function largestOfFour(arr) {
  var tempArray = [];
  for (var i = 0; i<arr.length;i++){
  	tempArray.push(arrayMax(arr[i]));
  }
  return tempArray;
}

function arrayMax(arr) {
  return arr.reduce(function (p, v) {
    return ( p > v ? p : v );
  });
}