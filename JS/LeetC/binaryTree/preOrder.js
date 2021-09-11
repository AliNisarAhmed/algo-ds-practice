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
 * @return {number[]}
 */

// PreOrder Traversal - Root, then left, then right
//
//

// Morris traversal - in place Constant space algorithm
function preorderTraversal(root) {
  let node = root,
    res = [];
  let current;

  while (node) {
    if (!node.left) {
      res.push(node.val);
      node = node.right;
    } else {
      current = node.left;

      while (current.right && current.right !== node) {
        current = current.right;
      }

      if (!current.right) {
        res.push(node.val);
        current.right = node;
        node = node.left;
      } else {
        current.right = null;
        node = node.right;
      }
    }
  }

  return res;
}

// Iterative - use stack
function preorderTraversal(root) {
  let stack = [];
  let res = [];

  stack.push(root);

  while (stack.length > 0) {
    let current = stack.pop();
    if (current && current.val) {
      res.push(current.val);
      stack.push(current.right);
      stack.push(current.left);
    }
  }

  return res;
}

// recursive
function preorderTraversal(root) {
  let res = [];

  helper(root, res);

  return res;

  function helper(node, res) {
    if (!node || !node.val) return res;

    res.push(node.val);

    helper(node.left, res);
    helper(node.right, res);
  }
}
