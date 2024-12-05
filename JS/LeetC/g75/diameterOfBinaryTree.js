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
 * @return {number}
 */
function diameterOfBinaryTree(root) {
  return diameter(root)[0];
}

function diameter(node) {
  if (!node) {
    return [-1, -1];
  }

  const [leftDiameter, leftHeight] = diameter(node.left);
  const [rightDiameter, rightHeight] = diameter(node.right);

  const nodeDiameter = leftHeight + rightHeight + 2;
  const maxDiameter = Math.max(leftDiameter, rightDiameter, nodeDiameter)

  return [maxDiameter, Math.max(leftHeight, rightHeight) + 1];
}
