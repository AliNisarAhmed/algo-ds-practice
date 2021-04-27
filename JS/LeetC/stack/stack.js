class Stack {
	constructor() {
		this.stack = [];
	}

	push(val) {
		this.stack.push(val);
		return this;
	}

	pop() {
		return this.stack.pop();
	}

	top() {
		return this.stack[this.stack.length - 1];
	}

	isEmpty() {
		return this.stack.length === 0;
	}
}

module.exports = Stack;