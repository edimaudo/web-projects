/*
Write a program that prompts for two numbers. Print the sum, difference, product, and quotient of those numbers as shown in the example output:

Values coming from users will be strings. Ensure that you convert these values to numbers before doing the math.
• Keep the inputs and outputs separate from the numerical conversions and other processing.
• Generate a single output statement with line breaks in the appropriate spots.

*/

//inputs
var firstnumber = prompt("What is the first number?");
var secondnumber = prompt("What is the second number?");

//output
alert(firstnumber + " + " + secondnumber + " = " + String(parseInt(firstnumber) + parseInt(secondnumber)));
alert(firstnumber + " - " + secondnumber + " = " + String(parseInt(firstnumber) - parseInt(secondnumber)));
alert(firstnumber + " * " + secondnumber + " = " + String(parseInt(firstnumber) * parseInt(secondnumber)));
alert(firstnumber + " / " + secondnumber + " = " + String(parseInt(firstnumber) / parseInt(secondnumber)));
