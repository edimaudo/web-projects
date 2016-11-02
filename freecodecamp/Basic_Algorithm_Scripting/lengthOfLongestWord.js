/*
Return the length of the longest word in the provided sentence.

Your response should be a number.
*/
function arrayMax(arr) {
  return arr.reduce(function (p, v) {
    return ( p > v ? p : v );
  });
}

function findLongestWord(str) {
  var output = str.split(" ");
  var outputlength = [];
  for (var i = 0; i<output.length;i++){
    outputlength.push(output[i].length);
  }
  return arrayMax(outputlength);
}