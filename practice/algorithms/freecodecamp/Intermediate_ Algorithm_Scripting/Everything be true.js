/*
Check if the predicate (second argument) returns truthy (defined) for all elements of a collection (first argument).
*/

function truthCheck(collection, pre) {
  // Is everyone being true?
	var count = 0;
  
  for (var i = 0; i < collection.length; i++){
			if(collection[i].hasOwnProperty(pre)){
      	if (typeof collection[i][pre] === "undefined" || collection[i][pre] === null || collection[i][pre]==="" ||
        collection[i][pre] === 0){
        	count+=0;
        } else if (valueIsNaN(collection[i][pre])){
        	count+=0;
        } else {
        		count+=1;
        }
      }
  }
  
  //alert(count + " " + collection.length);
  return count !== collection.length? false: true;
}

function valueIsNaN(v) { return v !== v; }
