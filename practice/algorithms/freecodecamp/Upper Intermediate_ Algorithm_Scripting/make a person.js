/*
Fill in the object constructor with the methods specified in the tests.

Those methods are getFirstName(), getLastName(), getFullName(), setFirstName(first), setLastName(last), and setFullName(firstAndLast).

*/
var Person = function(firstAndLast) {
  var fullName = firstAndLast;
  names = fullName.split(" ");
  var first = names[0];
  var last = names[1];
  
  this.getFirstName = function(){
    return names[0];
  }; 
  this.getLastName = function(){
    return names[1];
  }; 
  this.getFullName = function(){
    return names[0] +" "+ names[1];
  }; 
  this.setFirstName = function(first){
    names[0] = first;
    //first = names[0];
  };
  this.setLastName = function(last){
    names[1] = last;
    //last = names[1];
  };
  this.setFullName = function(firstAndLast){
     firstAndLast = names[0] + " " + names[1];
  };
};

var bob = new Person('Bob Ross');
bob.getFullName();