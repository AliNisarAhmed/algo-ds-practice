/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

function isBalanced(root) {
  return isBalancedHelper(root)[0];
}

function isBalancedHelper(root) {
  if (!root) {
    return [true, -1];
  }

  const [leftIsBalanced, leftHeight] = isBalancedHelper(root.left);
  if (!leftIsBalanced) {
    return [false, 0];
  }

  const [rightIsBalanced, rightHeight] = isBalancedHelper(root.right);
  if (!rightIsBalanced) {
    return [false, 0];
  }

  return [
    Math.abs(leftHeight - rightHeight) < 2,
    1 + Math.max(leftHeight, rightHeight),
  ];
}
