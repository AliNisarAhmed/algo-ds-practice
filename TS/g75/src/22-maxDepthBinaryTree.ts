import type { TreeNode } from "./00-TreeNode";

function maxDepthRec(root: TreeNode | null): number {
  return helper(root);
}

function helper(root: TreeNode | null): number {
  if (!root) {
    return 0;
  }

  const leftDepth = helper(root.left);
  const rightDepth = helper(root.right);

  return 1 + Math.max(leftDepth, rightDepth);
}

function maxDepth(root: TreeNode | null): number {
  let depth = 0;
  const stack: { node: TreeNode | null; depth: number }[] = [];
  if (root) {
    stack.push({ node: root, depth: 1 });
  }

  while (stack.length > 0) {
    let { node, depth: currentDepth } = stack.pop()!;
    depth = Math.max(depth, currentDepth);
    if (node) {
      stack.push({ node: node.left, depth: currentDepth + 1 });
      stack.push({ node: node.right, depth: currentDepth + 1 });
    }
  }

  return depth;
}

function maxDepthBFS(root: TreeNode | null): number {
  if (!root) return 0;
  let depth = 0;
  let queue = [root];

  while (queue.length > 0) {
    const level = queue.length;
    for (let i = 0; i < level; i++) {
      const node = queue.shift();
      if (node?.left) queue.push(node.left);
      if (node?.right) queue.push(node.right);
    }
    depth++;
  }
  return depth;
}
