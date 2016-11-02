/*
Create a program for your name and print a greeting 
using your name
*/

//challenge 1

/*
Write a version of the program that displays different greetings for different people.
*/

var input = prompt("What is your name?");
var outputvalue = "";
if (input == "john") {
	outputvalue = ", pleasure to meet you";
} else if (input == "james") {
	outputvalue = ", not nice to see you";
} else {
	outputvalue = ", nice to see you";
}
alert("Hello " + input + outputvalue);