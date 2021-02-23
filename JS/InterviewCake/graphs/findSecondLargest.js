function findSecondLargest(treeRoot) {
	if (!treeRoot || (!treeRoot.left && !treeRoot.right)) {
		throw new Error('Trees must have at least 2 nodes');
	}

	if (treeRoot.left && !treeRoot.right) {
		return findLargest(treeRoot.left);
	}

	if (treeRoot.right && !treeRoot.left && !treeRoot.right) {
		return treeRoot.value;
	}

	return findSecondLargest(treeRoot.right);
}

function findLargest(treeRoot) {
	if (!treeRoot) {
		throw new Error('Trees must have 1 node');
	}

	if (treeRoot.right) {
		return findLargest(treeRoot.right);
	}

	return treeRoot.value;
}