// A "superbalanced" (made up term) is a graph if the difference between the depths of any two leaf nodes is no greater than one.

import BinaryTreeNode from './btnode';

function isBalanced(treeRoot) {
	if (!treeRoot) {
		return true;
	}

	let depths = [];

	const nodes = [ [treeRoot, 0] ];

	while (nodes.length > 0) {

		let [ currentNode, currentDepth ] = nodes.pop();

		if (!currentNode.left && !currentNode.right) {
			// we reached a terminal node / leaf

			if (depths.indexOf(currentDepth) < 0) {
				depths.push(currentDepth);

				// e.g depths = [3, 4, 5] or depths = [3, 5]
				if (depths.length > 2 || Math.abs(depths[0] - depths[1]) > 1) {
					return false;
				}

			}

		} else {
			if (currentNode.left) {
				nodes.push([currentNode.left, currentDepth + 1]);
			}

			if (currentNode.right) {
				nodes.push([ currentNode, currentDepth + 1]);
			}
		}
	}

	return true;

}