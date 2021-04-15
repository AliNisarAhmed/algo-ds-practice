const TreeNode = require('./treeNode');

function isValidBST(root) {
	return validate(root);

	function validate(node, low = Number.NEGATIVE_INFINITY, high = Number.POSITIVE_INFINITY) {
		if (!node) {
			return true;
		}

		if (node.val <= low || node.val >= high) {
			return false;
		}

		return validate(node.left, low, node.val) && validate(node.right, node.val, high);
	}
}

function isValidBST(root) {
	if (!root) {
		return true;
	}

	let stack = [[root, Math.NEGATIVE_INFINITY, Math.POSITIVE_INFINITY]];

	while (stack.length > 0) {
		let [currentRoot, low, high] = stack.shift();
		if (!currentRoot) {
			continue;
		}
		if (currentRoot.val <= low || currentRoot.val >= high) {
			return false;
		}

		stack.push([currentRoot.right, currentRoot.val, high]);
		stack.push([currentRoot.left, low, currentRoot.val]);
	}

	return true;
}

let t = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));

let t2 = new TreeNode(2, new TreeNode(1), new TreeNode(3));

let t3 = new TreeNode(5, new TreeNode(4), new TreeNode(6, new TreeNode(3), new TreeNode(7)));

console.log(isValidBST(t3));
