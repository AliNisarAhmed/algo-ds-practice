//Write code to remove duplicates from an unsorted linked list.

const ListNode = require('./listNode');

function removeDups(head) {
	if (head === null) {
		return head;
	}

	let alreadySeen = {};

	let prev;
	let current = head;

	while (current) {
		if (alreadySeen[current.val]) {
			// remove this node from the list

			if (current.next === null) {
				prev.next = null;
				current = null;
			} else {
				current.val = current.next.val;
				current.next = current.next.next;
			}
		} else {
			alreadySeen[current.val] = true;
			prev = current;
			current = current.next;
		}
	}

	return head;
}

let l1 = { val: 1, next: { val: 2, next: { val: 3, next: null } } };

console.log(removeDups(l1));
