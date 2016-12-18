
/*
Create a program that prompts for a quote and an author. Display the quotation and author as shown in the example output.

Use a single output statement to produce this output, using appropriate string-escaping techniques for quotes.
• If your language supports string interpolation or string substitution, don’t use it for this exercise. Use string
concatenation instead.
*/

var quoteinput = prompt("What is the quote? ");
var quoter = prompt("Who said it?");
alert(quoter + " says, \""  + quoteinput + "\"");