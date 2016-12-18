/*
Check if the predicate (second argument) returns truthy (defined) for all elements of a collection (first argument).
*/

function every(collection, pre) {
  var count = 0;
  for (var i = 0; i < collection.length; i++) {
    if (collection[0].hasOwnProperty(pre)) {
      count += 1;
    }
  }
  return count !== collection.length ? false : true;
}