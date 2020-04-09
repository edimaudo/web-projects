// reads the textfields and submit
var textField = document.getElementById('textField');
var submit = document.getElementById('submitButton');

submit.addEventListener('click',buttonClicked,false);//listens for when submit is clicked

function buttonClicked(e){
	e.preventDefault(); //prevents reloading the page
	x=textField.value;
	x=eval(x); //calculates the expression
	textField.value=x;
}

function addToField(n){
	textField.value += n;

}

function power(y){
	x = textField.value;
	x=Math.pow(x,y);
	textField.value=x;
}

function powerten(y){
	x = textField.value
	x=Math.pow(10,x)
	textField.value = x;
}