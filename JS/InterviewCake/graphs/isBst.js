function isBinarySearchTree(
	treeRoot,
	lowerBound = Number.NEGATIVE_INFINITY,
	upperBound = Number.POSITIVE_INFINITY
) {
	if (!treeRoot) {
		return true;
	}

	if (treeRoot.value >= upperBound || treeRoot.value <= lowerBound) {
		return false;
	}

	return (
		isBinarySearchTree(treeRoot.left, lowerBound, treeRoot.value) &&
		isBinarySearchTree(treeRoot.right, treeRoot.value, upperBound)
	);
}
