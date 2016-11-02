/*
Goal
Create a program that prompts for an input string and dis- plays output that shows the input string and the number of characters the string contains.

Constraints
Be sure the output contains the original string.
Use a single output statement to construct the output.
Use a built-infunctionoftheprogramminglanguageto
determine the length of the string.
*/

//challenge 1
/*
If the user enters nothing,state that the user must enter something into the program.
*/

input = prompt("Please enter a value");
while(input.length < 1){
 alert("Please enter a value!");
 input = prompt("Please enter a value");
}
alert(input + " has " + input.length + " character(s)");