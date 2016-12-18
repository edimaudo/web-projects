/*
Create a program that determines how many years you have left until retirement and the year you can retire. It should prompt for your current age and the age you want to retire and display the output

constraint
be sure to convert the input to numerical data before doing any math.
Don’t hard-code the current year into your program. Get it from the system time via your programming lan- guage

combine basic and challenge
program returns a negative number by stating that the user can already retire.
*/

//inputs
var currentage = prompt("What is your current age?");
var retirementage = prompt("At what age would you like to retire?");
var diffage = parseInt(retirementage) - parseInt(currentage);
var d = new Date();
var currentyear = parseInt(d.getFullYear());
var retirementyear = currentyear + diffage;

//output
if ( diffage < 0) {
	alert("You can already retire");
} else {
	alert("You have " + diffage + "years left until you can retire. " + "It's " + String(currentyear) + ", so you can retire in " + String(retirementyear));
}