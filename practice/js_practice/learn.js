// TODO: create the character object here
const aurora = {
  name: "Aurora",
  health: 150,
  strength: 25,
  xp:0,
  
  // Return the character description
  describe() {
    return this.name + " has " + this.health + " health points and " + this.strength + " as strength and " + 
      this.xp + " as XP Points";}

};

// Aurora is harmed by an arrow
aurora.health -= 20;

// Aurora equips a strength necklace
aurora.strength += 10;

// Aurora learn a new skill
aurora.xp = aurora.xp + 15;


console.log(aurora.describe());

const dog = {
	name:"Fang",
	species:"boarhound",
	size:75,

	bark(){
		return "Grr Grr";
	}
}


console.log(dog.name + "is a " + dog.species + "dog measuring " + dog.size);
console.log("Look, a cat! " + dog.name +  " barks: " + dog.bark());


const r = Number(prompt("Enter the circle radius:"));

// TODO: create the circle object here
let circle =  {
  userinput:r,
  
	circumference(){
		return Math.PI*2*this.userinput;
	},

	area(){
		return Math.PI*this.userinput*this.userinput;
	}
}


console.log("Its circumference is " + circle.circumference());
console.log("Its area is " + circle.area());

/*
Write a program that creates an account object with the following characteristics:

A name property set to "Alex".
A balance property set to 0.
A credit method adding the value passed as an argument to the account balance.
A describe method returning the account description.

Use this object to show its description, crediting 250, debiting 80, then show its description again.
*/
//const r = Number(prompt("Enter the circle radius:"));

const account = {
	name:"Alex",
	balance:0,


	credit(creditAmount){
		return this.balance+=creditAmount;
	},

	description(){
		return "Owner: " + this.name + " has a balance of " + this.balance;
	}

}

console.log(account.description());
console.log(account.credit(250));
console.log(account.credit(500));
console.log(account.credit(-500));
console.log(account.description());