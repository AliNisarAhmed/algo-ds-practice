const Stack = require('./stack');

class MyQueue {
	constructor() {
		this.in = new Stack();
		this.out = new Stack();
	}

	enqueue(val) {
		this.getReadyForEnqueue();
		this.in.push(val);
		return this;
	}

	dequeue() {
		this.getReadyForDequeue();
		return this.out.pop();
	}

	getReadyForEnqueue() {
		if (this.in.isEmpty() && !this.out.isEmpty()) {
			while (!this.out.isEmpty()) {
				this.in.push(this.out.pop());
			}
		}
	}

	getReadyForDequeue() {
		if (this.out.isEmpty() && !this.in.isEmpty()) {
			while (!this.in.isEmpty()) {
				this.out.push(this.in.pop());
			}
		}
	}
}

module.exports = MyQueue;

const q = new MyQueue();

q.enqueue(1).enqueue(2).enqueue(3);

q.dequeue();

q.enqueue(4);