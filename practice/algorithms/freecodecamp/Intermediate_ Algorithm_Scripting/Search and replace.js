/*
Perform a search and replace on the sentence using the arguments provided and return the new sentence.

First argument is the sentence to perform the search and replace on.

Second argument is the word that you will be replacing (before).

Third argument is what you will be replacing the second argument with (after).

NOTE: Preserve the case of the original word when you are replacing it. For example if you mean to replace the word 'Book' with the word 'dog', it should be replaced as 'Dog'
*/

function myReplace(str, before, after) {
  var newafter = "";
   if (before[0] === before[0].toUpperCase()) {
      newafter = after[0].toUpperCase();
   } else {
     newafter = after[0].toLowerCase();
   }
   tempArray = str.split(" ");
   for (var i = 0; i<str.length;i++){
     if (tempArray[i] === before){
       tempArray[i] = newafter + after.slice(1,after.length);
     }
   }
  
  return tempArray.join(" ");
}