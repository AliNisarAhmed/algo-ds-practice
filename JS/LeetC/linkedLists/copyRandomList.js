/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */

class Node {
	constructor(val, next = null, random = null) {
		this.val = val;
		this.next = next;
		this.random = random;
	}
}

const visited = new WeakMap();

// ------- Iterative O(n) space -----------

function copyRandomList(head) {
	if (!head) return head;

	let oldNode = head;

	let newNode = new Node(oldNode.val);
	visited.set(oldNode, newNode);

	while (oldNode !== null) {
		newNode.random = getClonedNode(oldNode.random);
		newNode.next = getClonedNode(oldNode.next);

		oldNode = oldNode.next;
		newNode = newNode.next;
	}

	return visited.get(head);
}

function getClonedNode(node) {
	if (node) {
		if (visited.has(node)) {
			return visited.get(node);
		} else {
			visited.set(node, new Node(node.val));
			return visited.get(node);
		}

		return null;
	}
}

// -------------- RECURSIVE -------------

// function copyRandomList(head) {
// 	if (!head) return head;

// 	if (visited.has(head)) {
// 		return visited.get(head);
// 	}

// 	let newNode = { val: head.val };

// 	visited.set(head, newNode);

// 	newNode.next = copyRandomList(head.next);
// 	newNode.random = copyRandomList(head.random);

// 	return newNode;
// }

// -----------------------------------------

// ----------  Iterative O(1) space ---------

// function duplicateNodes(head) {
// 	let current = head;

// 	while (current) {
// 		let newNode = { val: current.val, next: current.next, tag: 'new' };

// 		let temp = current.next;
// 		current.next = newNode;

// 		current = temp;
// 	}

// 	return head;
// }

// function assignRandoms(head) {
// 	let current = head;
// 	let newList = head.next;

// 	while (current) {
// 		let currentRandom = current.random;
// 		let newRandom = null;
// 		if (currentRandom) {
// 			newRandom = currentRandom.next;
// 		}
// 		newList.random = newRandom;

// 		current = newList.next;
// 		if (current) {
// 			newList = current.next;
// 		}
// 	}

// 	return head;
// }

// function separateLists(head) {
// 	let newHead = head.next;
// 	let copy = head.next;
// 	let current = head;

// 	while (current && copy) {
// 		current.next = copy.next;

// 		if (copy.next) {
// 			copy.next = copy.next.next;
// 		}

// 		current = current.next;
// 		copy = copy.next;
// 	}

// 	return newHead;
// }

// function copyRandomList(head) {
// 	if (!head) return head;

// 	duplicateNodes(head);
// 	assignRandoms(head);

// 	let newHead = separateLists(head);

// 	return newHead;
// }

let l1 = {
	val: 1,
	next: {
		val: 2,
		next: {
			val: 3,
		},
	},
};

let n5 = new Node(1, null);
let n4 = new Node(10, n5);
let n3 = new Node(11, n4);
let n2 = new Node(13, n3);
let n1 = new Node(7, n2);

n5.random = n1;
n4.random = n3;
n3.random = n5;
n2.random = n1;
n1.random = null;

console.log(copyRandomList(n1));
