/*
Find the missing letter in the passed letter range and return it.

If all letters are present in the range, return undefined.

*/

function fearNotLetter(str) {
  var tempArray = [];
  var missingLetter="";
  for (var i = 0; i < str.length;i++){
    tempArray.push(str.charCodeAt(i));
  }

  for (var j = 0; j<tempArray.length;j++){
    if (tempArray[j+1] - tempArray[j] > 1){
      return String.fromCharCode(tempArray[j] + 1);
    }
  }
}