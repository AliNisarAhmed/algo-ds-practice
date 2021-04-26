const ListNode = require('./listNode');

function partition(head, k) {
	if (head === null) return null;

	let left = null;
	let right = null;

	let current = head;

	let newHead;
	let newRightHead;

	while (current) {
		let newNode = { val: current.val, next: null };

		if (current.val < k) {
			// append to the left list
			if (left === null) {
				left = newNode;
				newHead = newNode;
			} else {
				left.next = newNode;
				left = left.next;
			}

			current = current.next;
		} else {
			// append to the right list

			if (right === null) {
				right = newNode;
				newRightHead = newNode;
			} else {
				right.next = newNode;
				right = right.next;
			}

			current = current.next;
		}
	}

	left.next = newRightHead;

	return newHead;
}

function partition2(node, k) {
	let head = node;
	let tail = node;

	while (node) {
		let next = node.next;
		if (node.val < k) {
			node.next = head;
			head = node;
		} else {
			tail.next = node;
			tail = node;
		}

		node = next;
	}

	tail.next = null;

	return head;
}

let l1 = {
	val: 7,
	next: {
		val: 5,
		next: {
			val: 6,
			next: { val: 4, next: { val: 2, next: { val: 1, next: { val: 3, next: null } } } },
		},
	},
};

console.log(partition2(l1, 4))
