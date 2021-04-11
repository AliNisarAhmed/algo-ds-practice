const TreeNode = require('./treeNode');

function isValidBST(root) {
	if (!root) {
		return true;
	}

	let isLeftValid = true;
	if (root.left) {
		isLeftValid = checkLeftTree(root.left, root.val);
	}

	let isRightValid = true;
	if (root.right) {
		isRightValid = checkRightTree(root.right, root.val);
	}

	return isLeftValid && isRightValid;
}

function checkLeftTree(node, minValue) {
	if (!node) {
		return true;
	}

	if (node.val > minValue) {
		return false;
	}

	return checkLeftTree(node.left, minValue) && checkRightTree(node.right, minValue);
}

function checkRightTree(node, maxValue) {
	if (!node) {
		return true;
	}

	if (node.val < maxValue) {
		return false;
	}

	return checkLeftTree(node.left, maxValue) && checkRightTree(node.right, maxValue);
}

let t = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));

console.log(isValidBST(t));
