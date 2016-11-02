/*
Fill in the object constructor with the methods specified in the tests.

Those methods are getFirstName(), getLastName(), getFullName(), setFirstName(first), setLastName(last), and setFullName(firstAndLast).

*/
var Person = function(firstAndLast) {
  var fullName = firstAndLast;
  names = fullName.split(" ");
  //var first = names[0];
  //var last = names[1];
  this.getFirstName = function(){
    return names[0];
  }; 
  this.getLastName = function(){
    return names[1];
  }; 
  this.getFullName = function(){
    return fullName;
  }; 
  this.setFirstName = function(first){
    names[0] = first;
  }
  this.setLastName = function(last){
    names[1] = last;
  } 
  this.setFullName = function(firstAndLast){
    fullName = firstAndLast;
  };
};