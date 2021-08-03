function reverseList(head) {

	if (!head || !head.next) {
		return head;
	}

	let current = head;
	let prev = null;

	while (current) {
		temp = current.next;
		current.next = prev;
		prev = current;
		current = temp;
	}

	return prev;
}

function reverseList(head) {
	if (head === null || head.next === null) return head;
	let reversed = reverseList(head.next);
	head.next.next = head;
	head.next = null;
	return reversed;
}