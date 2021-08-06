// Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

// The first node is considered odd, and the second node is even, and so on.

// Note that the relative order inside both the even and odd groups should remain as it was in the input.

function oddEvenList(head) {
	if (!head || !head.next) return head;

	let oddHead = head;
	let oddTail = head;

	let evenHead = head.next;
	let evenTail = head.next;

	while (evenTail && evenTail.next) {
		oddTail.next = evenTail.next;
		oddTail = oddTail.next;
		evenTail.next = oddTail.next;
		evenTail = evenTail.next;
	}

	oddTail.next = evenHead;
	return head;
}


let list1 = {
	val: 1,
	next: {
		val: 2,
		next: {
			val: 3,
			next: {
				val: 4,
				next: {
					val: 5,
					next: null,
				},
			},
		},
	},
};

console.log(oddEvenList(list1));
