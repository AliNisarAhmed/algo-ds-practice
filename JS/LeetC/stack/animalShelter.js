// Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
// out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
// or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
// that type). They cannot select which specific animal they would like. Create the data structures to
// maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
// and dequeueCat. You may use the built-in Linked list data structure.

const Stack = require('./stack');

class Dog {
	constructor(order) {
		this.type = 'dog';
		this.order = order;
	}
}

class Cat {
	constructor(order) {
		this.type = 'cat';
		this.order = order;
	}
}

class AnimalShelter {
	constructor() {
		this.dogQueue = [];
		this.catQueue = [];
		this.order = 0;
	}

	enqueue(animal) {
		animal.order = this.order;
		this.order++;
		if (animal.type === 'dog') {
			this.dogQueue.push(animal);
		} else {
			this.catQueue.push(animal);
		}
	}

	dequeueAny() {
		let d = this.dogQueue[this.dogQueue.length - 1]
		let c = this.dogQueue[this.catQueue.length - 1]

		return d.order > c.order ? d : c;
	}

	dequeueDog() {
		return this.dogQueue.shift();
	}

	dequeueCat() {
		return this.catQueue.shift();
	}

}