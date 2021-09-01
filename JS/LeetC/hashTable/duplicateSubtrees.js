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
 * @return {TreeNode[]}
 */

function findDuplicateSubtrees(root) {
  const map = new Map();
  const res = [];

  populate(root, map, res);

  return res;
}

function populate(root, map, res) {
  if (!root) return "#";

  const subtree = `${root.val}.${populate(root.left, map, res)}.${populate(
    root.right,
    map,
    res
  )}`;
  map.set(subtree, (map.get(subtree) || 0) + 1);

  if (map.get(subtree) === 2) {
    res.push(root);
  }
  return subtree;
}
