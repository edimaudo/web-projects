/*
Compare and update inventory stored in a 2d array against a second 2d array of a fresh delivery. Update current inventory item quantity, and if an item cannot be found, add the new item and quantity into the inventory array in alphabetical order.
*/

function inventory(arr1, arr2) {

  var tempArray = [];
  var tempArray2 = [];

  //update inventory
  for (var i = 0; i < arr1.length; i++) {
    for (var j = 0; j < arr2.length; j++) {
      if (arr2[j][1] === arr1[i][1]) {
        arr1[i][0] = arr1[i][0] + arr2[j][0];
      }
    }
  }

  //add new inventory
  for (var i = 0; i < arr1.length; i++) {
    tempArray.push(arr1[i][1]);
  }

  for (var i = 0; i < arr2.length; i++) {
    if (tempArray.indexOf(arr2[i][1]) === -1) {
      tempArray2.push(arr2[i])
    }
  }
  //add in alpahbetical order
  var newval = arr1.concat(tempArray2);
  newval = newval.sort(function(a, b) {
    return a[1] > b[1];
  });
  return newval;

}