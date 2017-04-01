/*
Write an algorithm that will take an array for the first argument and return an array with all the objects that matches all the properties and values in the Object passed as second parameter.
*/

function where(collection, source) {
  // "What's in a name? that which we call a rose
  // By any other name would smell as sweet.”
  // -- by William Shakespeare, Romeo and Juliet
  var srcKeys = Object.keys(source);

  // filter the collection
  return collection.filter(function (obj) {
    for(var i = 0; i < srcKeys.length; i++) {
      // check if obj in collection doesn't have the key
      // or if it does have the key,
      // then check if the property value doesn't match the value in source
      if(!obj.hasOwnProperty(srcKeys[i]) || obj[srcKeys[i]] !== source[srcKeys[i]]) {
        return false;
      }
    }
    return true;
  });
}