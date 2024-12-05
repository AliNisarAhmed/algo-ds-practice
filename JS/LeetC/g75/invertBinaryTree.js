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
 * @return {TreeNode}
 */

function invertTree(root) {
  if (!root) {
    return root;
  }

  let right = invertTree(root.right);
  let left = invertTree(root.left);
  root.right = left;
  root.left = right;

  return root;
}


function invertTree(root) {
  if (!root) {
    return root;
  }

  const queue = [root];

  while (queue.length > 0) {
    current = queue.shift();
    [current.left, current.right] = [current.right, current.left];

    if (current.left) {
      queue.push(current.left);
    }

    if (current.right) {
      queue.push(current.right);
    }
  }

  return root;
}
