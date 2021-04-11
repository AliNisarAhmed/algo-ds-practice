import TreeNode from './treeNode';


function maxDepth(root) {
	if (!root) {
		return 0;
	}

	let leftDepth = maxDepth(root.left);
	let rightDepth = maxDepth(root.right);

	return 1 + Math.max(leftDepth, rightDepth);
}

// iterative - using a stack

function maxDepth(root) {
	let stack = [];

	if (root) {
		stack.push([1, root]);
	}

	let depth = 0;
	while (stack.length > 0) {
		let [currentDepth, currentRoot] = stack.shift();
		if (currentRoot) {
			depth = Math.max(currentDepth, depth);
			stack.push([currentDepth + 1, currentRoot.left]);
			stack.push([currentDepth + 1, currentRoot.right]);
		}
	}

	return depth;
}

// ------------------------------

let v1 = new TreeNode(3);
let v2 = new TreeNode(9);
let v3 = new TreeNode(20);
let v4 = new TreeNode(15);
let v5 = new TreeNode(7);

v1.left = v2;

v1.right = v3;

v3.left = v4;
v3.right = v5;

console.log(maxDepth(v1));
