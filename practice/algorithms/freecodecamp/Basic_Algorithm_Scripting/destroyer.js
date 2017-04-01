/*
You will be provided with an initial array (the first argument in the destroyer function), followed by one or more arguments. Remove all elements from the initial array that are of the same value as these arguments.
*/



function destroyer(arr) {

  var args = Array.prototype.slice.call(arguments);
  var args2 = args.slice(1,args.length);
 var tempArray = [];
  //return args2.indexOf(arr[0]);
  for (var i = 0; i < arr.length;i++){
    if (args2.indexOf(arr[i]) === -1) {
      tempArray.push(arr[i]);
    }
  }
  return tempArray;
}