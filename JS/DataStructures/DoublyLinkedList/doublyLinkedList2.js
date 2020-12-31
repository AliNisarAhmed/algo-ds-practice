class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
		this.previous = null;
	}
}

class DoublyLinkedList {
	constructor() {
		this.head = null;
		this.tail = null;
	}

	insertAtStart(v) {
		let newNode = new Node(v);
		newNode.next = this.head;
		this.head.previous = newNode;
		this.head = newNode;
		return this;
	}

	insertAtEnd(v) {
		let newNode = new Node(v);
		this.tail.next = newNode;
		newNode.previous = this.tail;
		return this;
	}

	removeFromFront() {
		let removedNode = this.head;
		this.head = this.head.next;
		return removedNode;
	}
}