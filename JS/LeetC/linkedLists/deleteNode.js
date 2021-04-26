// Definition of singly-linked list

class ListNode {
	contructor(val) {
		this.val = val;
		this.next = null;
	}
}

// We are not given the head of the list, we are just given the node to be deleted.
// We can delete the node just given the node to be deleted only
// we can shift the next value to node to be deleted and point it's next to next's next

// NOTE: here it is assumed that the node to be deleted is not the last node, to delete the last node we need a pointer to the node before it.
function deleteNode(node) {
	node.val = node.next.val;
	node.next = node.next.next;
}

let n1 = new ListNode(1);
let n2 = new ListNode(2);
let n3 = new ListNode(3);

n1.next = n2;
n2.next = n3;

deleteNode(n3);
