/*
Create a simple mad-lib program that prompts for a noun, a verb, an adverb, and an adjective and injects those into a story that you create.

constraints
Use a single output statement for this program.

If your language supports string interpolation or string
substitution, use it to build up the output.
*/

//inputs
var nouninput = prompt("Enter a noun:");
var verbinput = prompt("Enter a verb:");
var adjectiveinput = prompt("Enter an adjective:");
var adverbinput = prompt("Enter an adverb:");
var finaloutput = "oh yeah!";

//output
alert("Do you " + verbinput + " your " +  adjectiveinput + " " + nouninput + " " + adverbinput + "? " + finaloutput);