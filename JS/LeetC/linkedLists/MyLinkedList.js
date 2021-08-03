class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}

class MyLinkedList {
	constructor(node = null) {
		this.head = node;
	}

	// internal
	getNodeAtIndex(index) {
		if (!this.head) {
			return null;
		}

		let current = this.head;

		while (current) {
			if (index === 0) {
				return current;
			}

			if (index < 0) {
				return null;
			}

			index--;
			current = current.next;
		}

		return null;
	}

	/**
	 * Get the value of the index-th node in the linked list. If the index is invalid, return -1.
	 * @param {number} index
	 * @return {number}
	 */
	get(index) {
		let node = this.getNodeAtIndex(index);
		return node ? node.val : -1;
	}

	/**
	 * Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
	 * @param {number} val
	 * @return {void}
	 */
	addAtHead(v) {
		let newNode = new Node(v);
		newNode.next = this.head;
		this.head = newNode;
	}

	/**
	 * Append a node of value val to the last element of the linked list.
	 * @param {number} val
	 * @return {void}
	 */
	addAtTail(v) {
		let newNode = new Node(v);
		if (!this.head) {
			this.head = newNode;
			return;
		}

		let current = this.head;

		while (current.next) {
			current = current.next;
		}

		current.next = newNode;
	}

	/**
	 * Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
	 * @param {number} index
	 * @param {number} val
	 * @return {void}
	 */
	addAtIndex(index, val) {
		if (index < 0) {
			return;
		}

		if (index === 0) {
			return this.addAtHead(val);
		}

		const newNode = new Node(val);

		let prev = this.getNodeAtIndex(index - 1);
		if (prev) {
			newNode.next = prev.next;
			prev.next = newNode;
		}
	}

	/**
	 * Delete the index-th node in the linked list, if the index is valid.
	 * @param {number} index
	 * @return {void}
	 */
	deleteAtIndex(index) {
		if (index < 0) {
			return;
		}

		if (index === 0) {
			if (this.head) {
				this.head = this.head.next;
			}
			return;
		}

		let target = this.getNodeAtIndex(index - 1);
		if (target && target.next) {
			target.next = target.next.next;
		}
	}
}

var l = new MyLinkedList();
l.addAtIndex(0, 10);
l.addAtIndex(0, 20);
l.addAtIndex(1, 30);
console.log(l.get(0));
