
function calcLength(head) {
	let len = 0;
	let current = head;
	while (current) {
		len++;
		current = current.next;
	}

	return len;
}

// assuming K < length of list
function rotateRightKTimes(head, k) {
	// two pointers separated by k nodes;

	let prev = head;
	let current = head;

	while (k > 0) {
		current = current.next;
		k--;
	}

	while (current.next) {
		current = current.next;
		prev = prev.next;
	}

	let newHead = prev.next;
	prev.next = null;
	current.next = head;

	return newHead;
}

function rotateRight(head, k) {
	if (!head) return head;
	let newHead = head;
	let length = calcLength(head);

	if (length === 1) return head;

	let rotations = k % length;

	if (rotations > 0) {
		newHead = rotateRightKTimes(head, rotations);
	}


	return newHead;
}

let l1 = {
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

let l2 = { val: 1, next: { val: 2, next: null} };

console.log(rotateRight(l1, 5));

// console.log(rotateRightKTimes(l1, 2));

// we dont need rotate Once becase we can try to rotate a list (within its length) using two pointers

// function rotateRightOnce(head) {
// 	if (!head) return head;

// 	let prev = head;
// 	let current = head.next;

// 	if (!current) return prev;

// 	while (current) {
// 		if (!current.next) {
// 			prev.next = null;
// 			current.next = head;
// 			return current;
// 		}

// 		prev = current;
// 		current = current.next;
// 	}
// }