/*
Flatten a nested array. You must account for varying levels of nesting.
*/

function steamroller(arr) {
  tempArray = [];
  for (var i = 0; i < arr.length; i++){
    Array.isArray(arr[i])? tempArray = tempArray.concat(steamroller(arr[i])):tempArray.push(arr[i]);
  }
  return tempArray;
}
