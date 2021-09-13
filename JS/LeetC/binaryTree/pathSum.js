// Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
// A leaf is a node with no children.

// Iterative: Uses a stack

function hasPathSum(root, target) {
  if (!root) return false;

  let stack = [];
  stack.push([root, target - root.val]);

  while (stack.length > 0) {
    let [node, sum] = stack.pop();

    if (!node.left && !node.right && sum === 0) return true;

    if (node.right) {
      stack.push([node.right, sum - node.right.val]);
    }

    if (node.left) {
      stack.push([node.left, sum - node.left.val]);
    }

  }

  return false;
}

// Recursive
function hasPathSum(root, target) {
  if (!root) return false;

  let sum = target - root.val;

  if (!root.left && !root.right) return sum === 0;

  return hasPathSum(root.left, sum) || hasPathSum(root.right, sum);
}
