function mergeTwoListRecursive(l1, l2) {
	if (l1 === null) {
		return l2;
	} else if (l2 === null) {
		return l1;
	} else if (l1.val < l2.val) {
		l1.next = mergeTwoListRecursive(l1.next, l2);
		return l1;
	} else {
		l2.next = mergeTwoListRecursive(l1, l2.next);
		return l2;
	}
}


class ListNode {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}

function mergeTwoLists(l1, l2) {

	if (l1 === null) {
		return l2;
	}

	if (l2 === null) {
		return l1;
	}

	let mergedList;

	if (l1.val < l2.val) {
		mergedList = new ListNode(l1.val);
		l1 = l1.next;
	} else {
		mergedList = new ListNode(l2.val);
		l2 = l2.next;
	}

	let head = mergedList;

	while (l1 !== null || l2 !== null) {
		if (l1 === null) {
			mergedList.next = l2;
			return head;
		} else if (l2 === null) {
			mergedList.next = l1;
			return head;
		} else {
			if (l1.val < l2.val) {
				mergedList.next = l1;
				l1 = l1.next;
				mergedList = mergedList.next;
			} else {
				mergedList.next = l2;
				l2 = l2.next;
				mergedList = mergedList.next;
			}
		}
	}
	return head;
}

let l1 = { val: 1, next: { val: 2, next: { val: 4, next: null }}}
let l2 = { val: 1, next: { val: 3, next: { val: 4, next: null }}}

mergeTwoLists(l1, l2)