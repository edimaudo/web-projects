/*
Write a program that prompts the user for five numbers and computes the total of the numbers.

The prompting must use repetition, such as a counted loop, not three separate prompts.

Modify theprogram to prompt for how many numbers to add, instead of hard-coding the value. Be sure you convert the input to a number before doing the compar- ison.
• Modify the program so that it only adds numbers and silently rejects non-numeric values. Count these invalid entries as attempts anyway. In other words, if the number of numbers to add is 5, your program should still prompt only five times.

*/

//input
numberneeded = prompt("How many numbers do you want to add?");
var numlist = [];
var inputtext = "Enter a number: ";
var count = 0;
var total = 0.00;
var numberinput;

while (isNaN(parseInt(numberneeded))){
	numberneeded = prompt("How many numbers do you want to add?");
}

while (count !== parseInt(numberneeded)){
	count++;
	numberinput = prompt(inputtext);
	if (isNaN(parseInt(numberinput))){
		continue;
	} else {
		numlist.push(parseInt(numberinput));
	}
}

total = numlist.reduce(function(pv, cv) { return pv + cv; }, 0);

alert(total);




