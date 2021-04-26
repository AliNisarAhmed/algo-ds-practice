// Implement an algorithm to find the kth to last element of a singly linked list.

const ListNode = require('./listNode');

function kthToTheLast(head, k) {
	let ahead = head;

	while (k > 0) {
		ahead = ahead.next
		k--;
	}

	let current = head;

	while (ahead) {
		ahead = ahead.next;
		current = current.next;
	}

	return current;
}

// function kthToTheLast(head, k) {
// 	if (head === null) return null;

// 	let [index, node] = helper(head, k, 0);

// 	return node;
// }

// function helper(node, k, currentIndex) {
// 	if (k === currentIndex) {
// 		return [0, node];
// 	}

// 	let [newIndex, remNode] = helper(node.next, k, currentIndex + 1);

// 	return [newIndex + 1, node];
// }

let l1 = { val: 1, next: { val: 2, next: { val: 3, next: null } } };

console.log(kthToTheLast(l1, 2));