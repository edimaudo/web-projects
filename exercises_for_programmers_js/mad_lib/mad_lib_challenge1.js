/*
Create a simple mad-lib program that prompts for a noun, a verb, an adverb, and an adjective and injects those into a story that you create.

constraints
Use a single output statement for this program.

If your language supports string interpolation or string
substitution, use it to build up the output.

challenge 1
Add more inputs to the program to expand the story.
Implement a branching story, where the answers to questions determine how the story is constructed.
*/

//inputs
var firstword = prompt("Enter the first word:");
var secondword = prompt("Enter the second word");
var thirdword = prompt("Enter the third word");
var finalword = "Oh yeah!";
var finalword1 = "Oh no!";

var randomval = Math.random();

//output
if (randomval > 0.5) {
	alert(firstword + " " + secondword + " " + thirdword + " " + finalword);
} else {
	alert(firstword + " " + secondword + " " + thirdword + " " + finalword1);
}
