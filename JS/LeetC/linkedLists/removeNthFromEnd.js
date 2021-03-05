/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

class ListNode {
	contructor(val) {
		this.val = val;
		this.next = null;
	}
}


function removeNthFromEnd(head, n) {
	if (head.next === null) {
		return head = null;
	}

	let ahead = head;

	for (let k = 1; k <= n; k++) {
		ahead = ahead.next;
	}

	if (ahead === null) {
		head = head.next;
		return head;
	}

	let current = head;
	while (ahead.next !== null) {
		current = current.next;
		ahead = ahead.next;
	}

	if (current.next.next === null) { // meaning its at the tail of the list
		current.next = null;
 	} else {
		current.next = current.next.next;
	 }

	return head;
}

