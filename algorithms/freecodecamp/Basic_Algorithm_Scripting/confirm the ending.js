/*
Check if a string (first argument) ends with the given target string (second argument).
*/
function confirmEnding(str, target) {
   var output = str.split(" ");
  //return output;
  if (output.length < 2){
    return target === output[0].slice(output.lastIndexOf(target),str.length)? true:false;
  } else {
    lastValue = output[output.length - 1];
    return target === lastValue.substring(lastValue.length - target.length,lastValue.length)? true:false;
    //return target === output[output.length-1]? true:false;
  }
}