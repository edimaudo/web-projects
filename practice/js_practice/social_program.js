let links = [];
let userinput = "";
let linkadd = "";
let linkdelete = "";

main();

function main(){

  userinput = userprompt();
  if (userinput === "1"){
      	showlinks();
  } else if (userinput === "2"){
  	deletelinks();
  } else if (userinput === "3"){
  	addlinks();
  } else if (userinput === "4"){
  	exit();
  } else {
  	alert("Please enter a number between 1 to 4");
  	main();
  }  
}


function deletelinks(){
	if (links.length < 1){
		alert("No links to delete");
	} else {
		linkdelete = prompt("enter link position you want to delete");
		if (links[parseInt(linkdelete)] === undefined){
			alert("position does not exist");
			deletelinks();
		} else {
			delete links[parseInt(linkdelete)]
		}
	}
	main();
}

function addlinks(){
	linkadd = prompt("Enter the link you want to add");
	links.push(linkadd);
}

function showlinks(){
	if (links.length < 1){
		alert("No links available");
	} else {
		alert(links);
	}
	main();
}

function userprompt(){
	userinput = prompt("Choose an option: " + "\n" 
	+ "1: Show links" + "\n" 
	+ "2: Add a link" + "\n" 
	+ "3: Delete a link" + "\n"
	+ "4: End the program");
	return userinput;
}