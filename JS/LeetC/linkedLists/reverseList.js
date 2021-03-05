function reverseList(head) {
	if (!head || head.next === null) {
		return head;
	}

	let prev = null;
	let current = head;

	while (current !== null) {
		let temp = current.next;
		current.next = prev;
		prev = current;
		current = temp;
	}

	return prev;
}

function recursiveReverseList(head) {
	if (head === null || head.next === null) return head;
	let reversed = recursiveReverseList(head.next);
	head.next.next = head;
	head.next = null;
	return reversed;
}

const list = { val: 1, next: { val: 2, next: { val: 3, next: { val: 4, next: { val: 5, next: null}}}}}
reverseList(list);