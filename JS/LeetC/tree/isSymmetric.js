function isSymmetric(root) {
	if (!root) {
		return true;
	}

	return isSymmetricBinary(root.left, root.right);
}

function isSymmetricBinary(left, right) {
	if (!left && !right) {
		return true;
	}

	if (left && !right) {
		return false;
	}

	if (right && !left) {
		return false;
	}

	if (left.val !== right.val) {
		return false;
	}

	return isSymmetricBinary(left.left, right.right) && isSymmetricBinary(left.right, right.left);
}
