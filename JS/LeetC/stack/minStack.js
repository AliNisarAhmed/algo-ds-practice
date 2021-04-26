class MinStack {
	constructor() {
		this.stack = [];
		this.min = Number.POSITIVE_INFINITY;
	}

	push(val) {
		this.stack.push(val);
		if (val < this.min) {
			this.min = val;
		}
	}

	pop() {
		let removed = this.stack.pop();

		if (this.min === removed) {
			// find new minimum

			let newMin = Number.POSITIVE_INFINITY;

			for (let e of this.stack) {
				if (e < newMin) {
					newMin = e;
				}
			}

			this.min = newMin;
		}

		return removed;
	}

	top() {
		return this.stack[this.stack.length - 1];
	}

	getMin() {
		return this.min;
	}
}

class MinStack {
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

let stack = new MinStack();

stack.push(-2);
stack.push(0);
stack.push(-3);

stack.getMin();
stack.pop();
stack.top();
stack.getMin();
