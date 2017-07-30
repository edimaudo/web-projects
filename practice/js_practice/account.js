class account {
	constructor(name){
		this.name = name;
		this.balance = 0;
	}

	credit(amount){
		return this.balance += amount;
	}

	describe(){
		return "${this.name} has ${this.credit()}";
	}
}