/*
Create a simple self-checkout system. Prompt for the prices and quantities of three items. Calculate the subtotal of the items. Then calculate the tax using a tax rate of 5.5%. Print out the line items with the quantity and total, and then print out the subtotal, tax amount, and total.

Keep the input, processing, and output parts of your program separate. Collect the input, then do the math operations and string building, and then print out the output.
• Be sure you explicitly convert input to numerical data before doing any calculations.

challenge
Revisetheprogramtoensurethatpricesandquantities are entered as numeric values. Don’t allow the user to proceed if the value entered is not numeric.
*/

var numberofinput = Prompt("Enter the number of items");
var count = 1;
var totalprice = 0.00;
var tax = 0.055;

while (count < parseInt(numberofinput) + 1){
	var priceinputinfo = prompt("Enter the price of item " + count);
	var quantityinputinfo = prompt("Enter the quantity of item " + count);
	if (isNaN(parseFloat(priceinputinfo)) || isNaN(parseFloat(quantityinputinfo))) {
		alert("Please enter a valid numerical price or quantity");
		continue;
	} else {
		count++;
		totalprice = parseFloat(priceinputinfo) * parseFloat(quantityinputinfo);
	}
}

alert("SubTotal: $" + String(totalprice));
alert("Tax: $" + String(tax * totalprice));
alert("Total: $" + String(totalprice + (tax*totalprice)));


