// ----- RECURSIVE SOLUTION ----------

// If we iterate the nodes in reverse using recursion, and iterate forward at the same time using a variable outside the recursive function, then we can check whether or not we have a palindrome.

function isPalindrome(head) {
	let frontPointer = head;
	return recursivelyCheck(head);

	function recursivelyCheck(node) {
		if (node !== null) {
			if (!recursivelyCheck(node.next)) return false;
			if (node.val !== frontPointer.val) return false;
			frontPointer = frontPointer.next;
		}
		return true;
	}
}

// -----------------------------------------------

function isPalindrome(head) {
	let reversed = reverseList(head);
	let current = head;

	while (reversed !== null && current !== null) {
		if (current.val !== reversed.val) {
			return false;
		}
		current = current.next;
		reversed = reversed.next;
	}

	return true;
}

function reverseList(head) {
	let reversed = new ListNode(head.val);
	let temp = head.next;

	while (temp !== null) {
		let newNode = new ListNode(temp.val);
		newNode.next = reversed;
		reversed = newNode;
		temp = temp.next;
	}

	return reversed;
}

class ListNode {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}

let list = { val: 1, next: { val: 2, next: { val: 2, next: { val: 1, next: null } } } };
console.log(isPalindrome(list));
