class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

class LinkedList {
	constructor(head) {
		this.head = head;
	}

	read(index) {
		let currentIndex = 0;
		let currentNode = this.head;

		while (currentIndex < index) {
			currentNode = currentNode.next;
			currentIndex += 1;
		}

		return currentNode;
	}

	indexOf(v) {
		let currentNode = this.head;
		let index = 0;

		while (currentNode) {
			if (currentNode.value === v) {
				return index;
			}

			index++;
			currentNode = currentNode.next;
		}

		return -1;
	}

	insert(index, value) {
		let newNode = new Node(value);

		if (index === 0) {
			newNode.next = this.head;
			this.head = newNode;
			return this;
		}

		let currentNode = this.head;
		let currentIndex = 0;

		// we are looking for the node one before the new node's place
		while (currentIndex < index - 1) {
			currentNode = currentNode.next;
			currentIndex += 1;
		}

		newNode.next = currentNode.next;
		currentNode.next = newNode;
		return this;
	}

	delete(index) {
		if (!this.head) {
			return this;
		}

		if (index === 0) {
			this.head = this.head.next;
		} else {
			let currentIndex = 0;
			let currentNode = this.head;

			while (currentIndex < index - 1) {
				currentNode = currentNode.next;
				currentIndex += 1;
			}

			currentNode.next = currentNode.next.next;
		}

		return this;
	}

	print() {
		let list = `${this.head.value} ->`;
		let currentNode = this.head.next;
		while(currentNode) {
			list += ` ${currentNode.value} ->`
			currentNode = currentNode.next;
		}

		console.log(list);
		return this;
	}

	last() {
		if (!this.head) {
			return null;
		}

		let currentNode = this.head;

		while (currentNode.next) {
			currentNode = currentNode.next;
		}

		return currentNode;
	}

	reverse() {
		if (!this.head || !this.head.next) {
			return this;
		}

		let previous = null;
		let next = null;
		let currentNode = this.head;
		while (currentNode) {
			next = currentNode.next;
			currentNode.next = previous;
			if (next === null) {
				this.head = currentNode;
			}
			previous = currentNode;
			currentNode = next;
		}

		return this;
	}
}

let n1 = new Node(5);

let l = new LinkedList(n1);
l.insert(1, 4);
l.insert(2, 3);
l.insert(3, 2);
l.insert(4, 1);

console.log(l);
l.read(2);
l.delete(2);
console.log(l);
