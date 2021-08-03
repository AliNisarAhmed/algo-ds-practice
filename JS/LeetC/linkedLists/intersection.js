class ListNode {
	contructor(val) {
		this.val = val;
		this.next = null;
	}
}

// let c be the length of the common area,
// a be the length of list A before C
// b be the length of List B before C
// since a and b can different,
// a quick way to equalize both lists will be to add
// b to a
// and a to b
// after which, the length before C of both lists will be a + b
// once we do that, we can traverse both lists at once and find the common point.
function getIntersectionNode(headA, headB) {
	let p1 = headA;
	let p2 = headB;

	while (p1 !== p2) {
		p1 = p1 === null ? headB : p1.next;
		p2 = p2 === null ? headA : p2.next;
	}

	return p1;
}


function length(head) {
	let r = 0;
	if (!head) return r;
	let p = head;
	while (p.next) {
		p = p.next;
		r++;
	}
	return r;
}

function getIntersectionNode(headA, headB) {
	let lengthA = length(headA);
	let lengthB = length(headB);

	let diff = Math.abs(lengthA - lengthB);

	let p1 = lengthA > lengthB ? headA : headB;
	let p2 = lengthA > lengthB ? headB : headA;

	while (diff > 0) {
		p1 = p1.next;
		diff--;
	}

	while (p1 !== p2) {
		p1 = p1.next;
		p2 = p2.next;
	}

	return p1;

}

let v1 = new ListNode(1);
let v2 = new ListNode(8);
let v3 = new ListNode(4);
let v4 = new ListNode(5);

v1.next = v2;
v2.next = v3;
v3.next = v4;

let va1 = new ListNode(4);
let vb1 = new ListNode(5);
let vb2 = new ListNode(6);
vb1.next = vb2;

va1.next = v1;
vb2.next = v1;

getIntersectionNode(va1, vb1);
