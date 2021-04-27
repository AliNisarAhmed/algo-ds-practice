const Stack = require('./minStack');

class SetOfStacks {
	constructor(cap = 10) {
		this.stacks = [ [] ];
		this.capacity = cap;
	}

	lastStack() {
		return this.stacks[this.stacks.length - 1];
	}

	push(val) {
		const lastStack = this.lastStack();
		if (lastStack.length === this.capacity) {
			// create a new stack and push the item to it.
			this.stacks.push([val]);
		} else {
			lastStack.push(val);
		}
	}

	pop() {
		const lastStack = this.lastStack();

		const result = lastStack.pop();

		if (lastStack.length === 0) {
			this.stacks.pop();
		}

		if (this.stacks.length === 0) {
			this.stacks.push([]);
		}

		return result;
	}
}