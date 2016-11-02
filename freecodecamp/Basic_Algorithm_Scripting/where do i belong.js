/*
Return the lowest index at which a value (second argument) should be inserted into a sorted array (first argument).
*/
function where(arr, num) {
   var count = 0;
   for (var i = 0; i<arr.length;i++){
     if (num > arr[i]){
       count+=1;
     } 
   }
  return count;
}