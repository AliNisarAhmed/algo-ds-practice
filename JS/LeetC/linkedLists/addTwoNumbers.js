// the solution below is overwriting l1 with the sum,

// the solution is much simpler if we simply create a new linked list for the sum

function addTwoNumbers(l1, l2) {
	let carry = 0;
	let head = l1;
	let prev = l1;

	while (l1 || l2) {
		let t1 = l1 ? l1.val : 0;
		let t2 = l2 ? l2.val : 0;
		let sum = t1 + t2 + carry;

		if (sum >= 10) {
			carry = 1;
			sum = sum % 10;
		} else {
			carry = 0;
		}

		if (l1 && l2) {
			l1.val = sum;
			prev = l1;
			l1 = l1.next;
			l2 = l2.next;
		} else if (l1) {
			l1.val = sum;
			prev.next = l1;
			prev = prev.next;
			l1 = l1.next;
		} else {
			l2.val = sum;
			prev.next = l2;
			prev = prev.next;
			l2 = l2.next;
		}
	}

	if (carry > 0) {
		prev.next = { val: carry, next: null };
	}

	return head;
}

let l3 = {
	val: 2,
	next: {
		val: 4,
		next: {
			val: 9,
			next: null,
		},
	},
};

let l4 = {
	val: 5,
	next: {
		val: 6,
		next: {
			val: 4,
			next: {
				val: 9,
				next: null,
			},
		},
	},
};

let l1 = {
	val: 9,
	next: {
		val: 9,
		next: {
			val: 9,
			next: {
				val: 9,
				next: {
					val: 9,
					next: {
						val: 9,
						next: {
							val: 9,
							next: null,
						},
					},
				},
			},
		},
	},
};

let l2 = {
	val: 9,
	next: {
		val: 9,
		next: {
			val: 9,
			next: {
				val: 9,
				next: null,
			},
		},
	},
};

let l5 = {
	val: 9,
	next: { val: 9, next: { val: 9, next: null } },
};

let l6 = {
	val: 9,
	next: null,
};

console.log(addTwoNumbers(l5, l6));
