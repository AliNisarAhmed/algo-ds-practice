const Stack = require('./stack');

class SortedStack {
	constructor() {
		this.primary = new Stack();
		this.secondary = new Stack();
	}

	sort() {
		while (!this.primary.isEmpty()) {
			let current = this.primary.pop();

			if (this.secondary.isEmpty()) {
				this.secondary.push(current);
			} else {

				while (this.secondary.top() > current) {
					this.primary.push(this.secondary.pop());
				}

				this.secondary.push(current);
			}
		}

		return this.secondary;
	}
}

var s = new SortedStack();

s.primary.push(1).push(5).push(2).push(8);

s.sort();



