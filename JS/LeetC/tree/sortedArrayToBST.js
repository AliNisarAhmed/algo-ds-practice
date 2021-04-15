const TreeNode = require('./treeNode');

function sortedArrayToBST(nums, start = 0, end = nums.length) {
	if (start === end) {
		return null;
	}

	let midpoint = Math.floor((end + start) / 2);
	let root = new TreeNode(nums[midpoint]);

	if (start - end === 1) {
		return root;
	}

	root.left = sortedArrayToBST(nums, start, midpoint);
	root.right = sortedArrayToBST(nums, midpoint + 1, end);

	return root;
}

sortedArrayToBST([-10, -3, 0, 5, 9]);
