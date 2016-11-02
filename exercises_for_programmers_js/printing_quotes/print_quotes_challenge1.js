/*
Create a program that prompts for a quote and an author. Display the quotation and author as shown in the example output.

Use a single output statement to produce this output, using appropriate string-escaping techniques for quotes.
• If your language supports string interpolation or string substitution, don’t use it for this exercise. Use string
concatenation instead.

challenge 1
Modify this program so that instead of prompting for quotes from the user, you cre- ate a structure that holds quotes and their associated attributions and then display all of the quotes using the format in the example. An array of maps would be a good choice.Modify this program so that instead of prompting for quotes from the user, you cre- ate a structure that holds quotes and their associated attributions and then display all of the quotes using the format in the example. An array of maps would be a good choice.
*/

var quoteinfo = {"John smith": "Thou shalt forbear", "Mary Hancock": "Move if you want to", "Sally Fields": "Hail Mary all day"};
for (var key in quoteinfo){
	alert(key + " says, \""  + quoteinfo[key] + "\"");
}