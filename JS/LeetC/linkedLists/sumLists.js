const ListNode = require('./listNode');

function sumLists(l1, l2) {
	if (l1 === null) {
		return l2;
	}

	if (l2 === null) {
		return l1;
	}

	let currentSum = l1.val + l2.val;
	let rem = sumLists(l1.next, l2.next);

	if (currentSum >= 10) {
		if (rem === null) {
			rem = { val: 1, next: null};
		} else {
			rem.val = rem.val ? rem.val + 1 : 1;
		}
		currentSum = currentSum % 10;
	}

	let newNode = { val: currentSum, next: rem };

	return newNode;
}

let l1 = { val: 9, next: { val: 7, next: {val: 8, next: null}}}
let l2 = { val: 6, next: { val: 8, next: {val: 5, next: null}}}

console.log(sumLists(l1, l2));