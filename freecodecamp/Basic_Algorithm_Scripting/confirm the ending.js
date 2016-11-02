/*
Check if a string (first argument) ends with the given target string (second argument).
*/
function end(str, target) {
   var output = str.split(" ");
  //return output;
  if (output.length < 2){
    return target === output[0].slice(output.lastIndexOf(target),str.length)? true:false;
  } else {
    return target === output[output.length-1]? true:false;
  }
}