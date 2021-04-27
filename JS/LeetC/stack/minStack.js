

class Stack {
	constructor() {
		this.stack = [];
	}

	push(val) {
		if (this.stack.length === 0) {
			this.stack.push([val, val]);
		} else {
			let newMin = Math.min(val, this.stack[this.stack.length - 1][1]);
			this.stack.push([val, newMin]);
		}
	}

	isEmpty() {
		return this.stack.length === 0;
	}

	pop() {
		this.stack.pop();
	}

	top() {
		return this.stack[this.stack.length - 1][0];
	}

	getMin() {
		return this.stack[this.stack.length - 1][1];
	}
}

let stack = new Stack();

stack.push(-2);
stack.push(0);
stack.push(-3);

stack.getMin();
stack.pop();
stack.top();
stack.getMin();

module.exports = Stack;