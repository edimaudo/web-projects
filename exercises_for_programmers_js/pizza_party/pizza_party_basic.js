/*
Write a program to evenly divide pizzas. Prompt for the number of people, the number of pizzas, and the number of slices per pizza. Ensure that the number of pieces comes out even. Display the number of pieces of pizza each person should get. If there are leftovers, show the number of leftover pieces.


*/

//inputs
var peopleinfo = prompt("How many people?"); //5
var pizzainfo = prompt("How many pizzas do you have?"); //2
var pizzaslice = prompt("How many pizza slices"); //2


/*
assumption
pizza has 8 slices

var div = Math.floor(y/x);
var rem = y % x;
*/

//calculation
var peopleslice = parseInt(peopleinfo) * parseInt(pizzaslice);
var pizzasliceavailable = parseInt(pizzainfo)*8;
var calc = Math.Floor(pizzasliceavailable / peopleslice);
var rem =  pizzasliceavailable % peopleslice;


//output
alert("There are " + peopleinfo + " people with " + pizzainfo + " pizza(s)");
alert("Each person gets " + calc + " pieces of pizza");
alert("There are " + rem + " leftover pieces");
