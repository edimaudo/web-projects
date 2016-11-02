/*
Remove all falsy values from an array.

Falsy values in javascript are false, null, 0, "", undefined, and NaN.
*/



function bouncerFilter(value){
  if(value === 0 || value === undefined || value === null || value === false 
     || value === "" || Number.isNaN(value)){
    return false;
  }  else {
    return true;
  }
}

function bouncer(arr) {
  return arr.filter(bouncerFilter);
}