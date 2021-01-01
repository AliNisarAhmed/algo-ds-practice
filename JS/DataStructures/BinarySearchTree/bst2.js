class Node {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

class BinarySearchTree {
	constructor() {
		this.root = null;
	}

	insert(v, node = this.root) {
		if (!this.root) {
			this.root = new Node(v);
			return this;
		}

		if (v > node.value) {
			if (!node.right) {
				node.right = new Node(v);
				return this;
			} else {
				return this.insert(v, node.right);
			}
		}

		if (v < node.value) {
			if (!node.left) {
				node.left = new Node(v);
				return this;
			} else {
				return this.insert(v, node.left);
			}
		}
	}

	search(value, node = this.root) {
		if (node.value === value) {
			return node;
		}

		if (!node.value) {
			return null;
		}

		if (value > node.value) {
			return this.search(value, node.right);
		}

		if (value < node.value) {
			return this.search(value, node.left);
		}
	}

	// 1. if the node being deleted has no children, simply delete it.
	// 2. If the node being deleted has one child, delete the node, and plug the child into the spot where the delete node was.
	// 3. When deleting a node with two children, replace the deleted node with the successor node.
	// The successor node is the child node whose value if the least of all values that are greater than the deleted node.

	// Finding the successor node

	// Visit the right child of the deleted value, and then keep on visiting the left child of each subsequent child, until there are no more left children. The bottom value is the successor node.

	// If the successor node has a right child, after plugging the successor node into the spot of the deleted node, take the former right child of the successor node and turn it into tht left child of the former parent of the successor node.

	delete(valueToDelete, node = this.root) {
		if (!node) {
			return null;
		} else if (valueToDelete < node.value) {
			node.left = this.delete(valueToDelete, node.left);
			return node;
		} else if (valueToDelete > node.value) {
			node.right = this.delete(valueToDelete, node.right);
			return node;
		} else if (valueToDelete === node.value) {
			if (!node.left) {
				return node.right;
			} else if (!node.right) {
				return node.left;
			} else {
				node.right = this.lift(node.right, node);
				return node;
			}
		}
	}

	lift(node, nodeToDelete) {
		if (node.left) {
			node.left = this.lift(node.left, nodeToDelete);
			return node;
		} else {
			nodeToDelete.value = node.value;
			return node.right;
		}
	}

	inOrder(node = this.root) {
		if (!node) return;
		this.inOrder(node.left);
		console.log(node.value);
		this.inOrder(node.right);
	}

	maxValue(node = this.root) {
		if (!node) {
			return null;
		}
 		if (node.right) {
			return this.maxValue(node.right);
		} else {
			return node.value;
		}
	}
}

let t = new BinarySearchTree();

// t.insert(3).insert(2).insert(4).insert(1).insert(5);

// t.search(5);

t.insert(50)
	.insert(25)
	.insert(11)
	.insert(33)
	.insert(30)
	.insert(40)
	.insert(75)
	.insert(89)
	.insert(82)
	.insert(95)
	.insert(61)
	.insert(52)
	.insert(55);

let t2 = new BinarySearchTree();

t2.insert('M')
	.insert('G')
	.insert('A')
	.insert('L')
	.insert('R')
	.insert('P')
	.insert('T');

