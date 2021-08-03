
// Recursive solution
function removeElements(head, val, prev = null) {
	if (!head) return head;

	let removed = removeElements(head.next, val, head);

	if (head.val === val) {
		return removed;
	} else {
		head.next = removed;
		return head;
	}
}


// iterative

function removeElements(head, val) {
	if (!head) return head;

	let current = head;

	while (current && current.val === val) {
		current = current.next;
	}

	head = current;
	let prev = head;

	while (current) {
		if (current.val === val) {
			prev.next = current.next;
		} else {
			prev = current;
		}

		current = current.next;
	}

	return head;
}


let list1 = {
	val: 7,
	next: {
		val: 7,
		next: {
			val: 7,
			next: {
				val: 7,
				next: null,
			},
		},
	},
};

let list = {
	val: 1,
	next: {
		val: 2,
		next: {
			val: 6,
			next: { val: 3, next: { val: 4, next: { val: 5, next: { val: 6, next: null } } } },
		},
	},
};

let list3 = {
	val: 1,
	next: {
		val: 2,
		next: null,
	},
};

console.log(removeElements(list3, 1));
