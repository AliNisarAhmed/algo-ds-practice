class Node {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

class BST {
	constructor() {
		this.root = null;
	}

	insert(value) {
		let newNode = new Node(value);
		if (!this.root) {
			this.root = newNode;
			return this;
		} else {
			let current = this.root;
			while (true) {
				if (value < current.value) {
					if (!current.left) {
						current.left = newNode;
						return this;
					} else {
						current = current.left;
					}
				} else {
					if (!current.right) {
						current.right = newNode;
						return this;
					} else {
						current = current.right;
					}
				}
			}
		}
	}

	insert2(value) {
		let newNode = new Node(value);
		if (!this.root) {
			this.root = newNode;
			return this;
		} else {
			this.insertR(this.root, newNode);
			return this;
		}
	}

	insertR(current, newNode) {
		if (newNode.value < current.value) {
			if (current.left === null) {
				current.left = newNode;
			} else {
				this.insertR(current.left, newNode);
			}
		} else {
			if (current.right === null) {
				current.right = newNode;
			} else {
				this.insertR(current.right, newNode);
			}
		}
	}

	find(value) {
		if (!this.root) {
			return false;
		}
		return this.findR(this.root, value);
	}

	findR(current, v) {
		if (current === null) return false;
		if (current.value === v) return true;
		if (v > current.value) return this.findR(current.right, v);

		return this.findR(current.left, v);
	}

	// iterative
	find2(value) {
		if (!this.root) return false;
		let current = this.root;
		while (true) {
			if (!current) return false;
			if (current.value === value) return true;
			if (value > current.value) current = current.right;
			if (value < current.left) current = current.left;
		}
	}
}

const bst = new BST();
bst.insert(10).insert(15).insert(6).insert(20).insert(3).insert(8);

//  ---- Tree Traversal ----

function bfs(tree) {
	const visited = [];
	const queue = [];
	queue.push(tree.root);
	while (queue.length > 0) {
		let current = queue.shift();
		visited.push(current.value);
		if (current.left) {
			queue.push(current.left);
		}
		if (current.right) {
			queue.push(current.right);
		}
	}
	return visited;
}

console.log(bfs(bst));

// Depth First Search
// https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

function dfs(tree) {
	const result = {
		preorder: [],
		postorder: [],
		inorder: [],
	};
	const current = tree.root;

	preorder(current);
	postorder(current);
	inorder(current);

	return result;

	// Left, Root, Right
	// All the lefts, then the roots, then the corresponding rights
	function inorder(curr) {
		if (curr.left) {
			inorder(curr.left);
		}
		result.inorder.push(curr.value);
		if (curr.right) {
			inorder(curr.right);
		}
	}

	// Root, Left, Right
	// root, all the lefts, all the rights
	function preorder(curr) {
		result.preorder.push(curr.value);
		if (curr.left) {
			preorder(curr.left);
		}
		if (curr.right) {
			preorder(curr.right);
		}
	}

	// Left, Right, Root
	// all the lefts, all the rights, then the root
	function postorder(curr) {
		if (curr.right) {
			postorder(curr.right);
		}
		if (curr.left) {
			postorder(curr.left);
		}
		result.postorder.push(curr.value);
	}
}

console.log(dfs(bst));

module.exports = BST;
