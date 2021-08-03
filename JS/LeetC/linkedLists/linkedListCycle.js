function ListNode(val) {
	this.val = val;
	this.next = null;
}

function hasCycle(head) {
	let visited = new Set();
	let current = head;
	while (current) {
		if (visited.has(current)) {
			return true;
		} else {
			visited.add(current);
			current = current.next;
		}
	}

	return false;
}

// iterative - using "fast" and "slow" pointer
function hasCycle(head) {
	if (head === null) {
		return false;
	}
	let slow = head;
	let fast = head.next;
	while (fast && fast.next && fast.next.next) {
		if (fast === slow) {
			return true;
		}

		fast = fast.next.next;
		slow = slow.next;
	}
	return false;
}

// return the first node where the cycle begins
function detectCycle(head) {
	if (head === null || head.next === null) {
		return null;
	}

	let slow = head;
	let fast = head;

	while (true) {

		if (!fast || !fast.next || !fast.next.next) {
			return null;
		}

		fast = fast.next.next;
		slow = slow.next;

		if (fast === slow) {
			break;
		}
	}

	let p1 = head;

	while (p1 !== fast) {
		p1 = p1.next;
		fast = fast.next;
	}

	return p1;
}

let v1 = new ListNode(3);
let v2 = new ListNode(2);
let v3 = new ListNode(0);
let v4 = new ListNode(-4);

v1.next = v2;
v2.next = v3;
v3.next = v4;
v4.next = v2;

console.log(detectCycle(v1));
