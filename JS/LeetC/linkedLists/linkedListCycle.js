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


let v1 = new ListNode(3);
let v2 = new ListNode(2);
let v3 = new ListNode(0)
let v4 = new ListNode(-4);

v1.next = v2;
v2.next = v3
v3.next = v4
v4.next = v2;

hasCycle(v1);


let p1 = new ListNode(1);

hasCycle(p1);
