class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function diameterOfBinaryTree(root: TreeNode | null): number {
  return helper(root)[0];
}

function helper(root: TreeNode | null): [number, number] {
  if (!root) return [-1, -1];

  const [leftDiameter, leftHeight] = helper(root.left);
  const [rightDiameter, rightHeight] = helper(root.right);

  const nodeDiameter = leftHeight + rightHeight + 2;
  const maxDiameter = Math.max(leftDiameter, rightDiameter, nodeDiameter);

  return [maxDiameter, 1 + Math.max(leftHeight, rightHeight)];
}
