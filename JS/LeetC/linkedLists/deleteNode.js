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
function deleteNode(node) {
	node.val = node.next.val;
	node.next = node.next.next;
}