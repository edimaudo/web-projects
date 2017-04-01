/*
The DNA strand is missing the pairing element. Take each character, get its pair, and return the results as a 2d array.

Base pairs are a pair of AT and CG. Match the missing element to the provided character.

Return the provided character as the first element in each array.
*/

function getPair(n){
  if (n === "A"){
    return ["A","T"];
  } else if (n === "T"){
    return ["T","A"];
  } else if (n === "C"){
    return ["C","G"]
  } else {
    return ["G","C"];
  }
}

function pairElement(str) {
 tempArray = [];
  for (var i = 0; i < str.length; i++){
   tempArray.push(getPair(str[i]));
 }
  return tempArray;
}

pairElement("GCG");