/*
Create a function that takes two or more arrays and returns an array of the symmetric difference of the provided arrays.
*/

function getUnique(arr1, arr2) {
  var tempArray1 = [];
  var tempArray2 = [];

  tempArray1 = arr2.filter(function(item) {
    return arr1.indexOf(item) === -1;
  })

  tempArray2 = arr1.filter(function(item) {
    return arr2.indexOf(item) === -1;
  })

  return tempArray2.concat(tempArray1);

}

function sym(args) {

    var arr = Array.prototype.slice.call(arguments);
    if (arr.length < 2) {
      return arr[0];
    } else if (arr.length < 3) {
      return getUnique(arr[0], arr[1]);
    } else {
      var beginVal = getUnique(arr[0], arr[1]);
      for (var i = 2; i < arr.length; i++) {
        beginVal = getUnique(beginVal, arr[i]);
      }

      uniqueArray = beginVal.filter(function(item, pos) {
        return beginVal.indexOf(item) == pos;
      })

      return uniqueArray;
    }
  }
  //return getUnique(arr[0], arr[1]);



console.log(sym([1, 2, 3], [5, 2, 1, 4]));
console.log(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]));
//[1, 2, 3], [5, 2, 1, 4]), [3, 5, 4]
//[1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]), [1, 4, 5]