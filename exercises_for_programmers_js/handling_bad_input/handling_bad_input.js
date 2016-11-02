/*
Write a quick calculator that prompts for the rate of return on an investment and calculates how many years it will take to double your investment.

Don’t allow the user to enter 0.
• Don’t allow non-numeric values.
• Usealooptotrapbadinput,soyoucanensurethatthe
user enters valid values.
 show different error message when the user enters 0.
*/

//input
rateofreturn = prompt("What is the rate of return?");
var invalidinput = "Sorry that is not a valid input.";
var invalidinputzero = " Sorry.  You cannot have a rate of return of zero.";
var yearinfo = 0.00;

while (isNaN(parseInt(rateofreturn)) || parseInt(rateofreturn)===0){
	if (rateofreturn === "0"){
		alert(invalidinputzero);
	} else {
		alert(invalidinput);
	}
	rateofreturn = prompt("What is the rate of return?");
}

yearinfo = 72/parseInt(rateofreturn);

//output
alert("It will take " + yearinfo + " years to double your investment");