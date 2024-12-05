function isBalanced(root: TreeNode | null): boolean {
  return isBalancedHelper(root)[0];
}

function isBalancedHelper(root: TreeNode | null) {
  if (!root) {
    return [true, -1];
  }

  const [leftBalanced, leftHeight] = isBalancedHelper(root.left);
  if (!leftBalanced) {
    return [false, 0];
  }

  const [rightBalanced, rightHeight] = isBalancedHelper(root.right);
  if (!rightBalanced) {
    return [false, 0];
  }

  return [
    Math.abs(leftHeight - rightHeight) > 2,
    1 + Math.max(leftHeight, rightHeight),
  ];
}
