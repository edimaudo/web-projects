Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array.
*/

function mutation(arr) {
  var count = 0;
  word1 = arr[0].toLowerCase().split("");
  word2 = arr[1].toLowerCase().split("");
  for (var i = 0;i<word2.length;i++){
    if (word1.indexOf(word2[i]) === -1){count+=1};
  }
  
  return count >=1?false:true;
}