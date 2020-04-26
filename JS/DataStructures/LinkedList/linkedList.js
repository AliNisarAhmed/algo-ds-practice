class Node {
	constructor(v) {
		this.value = v;
		this.next = null;
	}
}

class SinglyLinkedList {
	constructor() {
		this.head = null;
		this.tail = null;
		this.length = 0;
	}

	see() {
		// to "see" the current list
		let current = this.head;
		let res = '';
		while (current) {
			res += `${current.value} -> `;
			current = current.next;
		}

		console.log(res);
	}

	push(val) {
		let node = new Node(val);
		if (!this.head) {
			this.head = this.tail = node;
		} else if (this.tail) {
			this.tail.next = node;
			this.tail = node;
		}
		this.length++;
		return this;
	}

	pop() {
		if (!this.head) {
			return null;
		}

		let removed;

		if (this.length === 1) {
			removed = this.head;
			this.head = this.tail = null;
		}

		let current = this.head;
		let prev = null; // to keep track of the second to last item
		while (current.next) {
			prev = current;
			current = current.next;
		}

		this.tail = prev;
		this.tail.next = null;
		this.length--;
		return removed;
	}

	shift() {
		if (!this.head) return null;
		if (this.length === 1) {
			this.head = this.tail = null;
			this.length--;
		}
		let removed = this.head;
		this.head = this.head.next;
		this.length--;
		return removed;
	}

	unshift(val) {
		let newNode = new Node(val);
		if (!this.head) {
			this.head = this.tail = newNode;
		} else {
			newNode.next = this.head;
			this.head = newNode;
		}
		this.length++;
		return this;
	}

	get(index) {
		if (index < 0 || index >= this.length) return null;
		let result = this.head;
		while (index > 0) {
			result = result.next;
			index--;
		}
		return result;
	}

	set(value, index) {
		if (index < 0 || index >= this.length) return false;

		let newNode = new Node(value);
		let item = this.head;
		let prev = null;
		while (index > 0) {
			prev = item;
			item = item.next;
			index--;
		}
		if (prev) {
			prev.next = newNode;
			newNode.next = item.next;
		} else {
			newNode.next = item.next;
			this.head = newNode;
		}
		return true;
	}

	insert(value, index) {
		if (index < 0 || index > this.length) return false;

		if (index === 0) {
			return this.unshift(value);
		} else if (index == this.length) {
			return this.push(value);
		} else {
			let newNode = new Node(value);
			let item = this.head;
			while (index - 1> 0) {
				item = item.next;
				index--;
			}
			newNode.next = item.next;
			item.next = newNode;
		}
		this.length++;
		return true;
	}

	remove(index) {
		if (index < 0 || index >= this.length) return false;
		if (index === 0) {
			this.head = this.head.next
		} else {
			let prev = null;
			let item = this.head;
			while (index > 0) {
				prev = item;
				item = item.next;
				index--;
			}
			if (item === null) {
				// we needed to remove the tail
				this.tail = prev;
			} else {
				prev.next = item.next;
			}
		}
		this.length--;
		return true;
	}

	reverse() {
		if (this.length <= 1) return this;
		// swap head and tail
		[ this.head, this.tail ] = [ this.tail, this.head ];
		let next;
		let prev = null;
		// start with what used to be the previous head
		let current = this.tail;
		while(current) {
			// capture the current node's next, to use it later
			next = current.next;
			// set the current node's next to be prev i.e. "reverse the arrow"
			current.next = prev;
			// now make the current node prev, i.e. prepare for the next iteration
			prev = current;
			// move on to the next element by making it current
			current = next;
		}

		return this;
	}
}

module.exports = SinglyLinkedList;
