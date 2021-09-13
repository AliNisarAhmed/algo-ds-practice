// recursive - bottom up - postorder
function maxDepth(root) {
  if (!root) return 0;

  let left = maxDepth(root.left);
  let right = maxDepth(root.right);

  return 1 + Math.max(left, right);
}

// recursive - top down - pre order
//

function maxDepth(root) {
  if (!root) return 0;

  let ans = 1;

  helper(root, ans);

  return ans;

  function helper(node, depth) {
    if (!node) return depth;

    if (node.left === null && node.right === null) {
      ans = Math.max(ans, depth);
    }

    helper(node.left, depth + 1);
    helper(node.right, depth + 1);
  }
}
