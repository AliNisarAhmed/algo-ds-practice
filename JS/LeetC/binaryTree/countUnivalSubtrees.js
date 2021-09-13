// Given the root of a binary tree, return the number of uni-value subtrees.

// A uni-value subtree means all nodes of the subtree have the same value.

// Recursive, counting nulls as true and passing in parent's value to ease comparisons
function countUnivalSubtrees(root) {
  let count = 0;

  helper(root, 0);

  return count;

  function helper(node, val) {
    if (!node) return true;

    let left = helper(node.left, node.val);
    let right = helper(node.right, node.val);

    if (!left || !right) return false;

    count++;

    return node.val === val;
  }
}


/// Recursive
function countUnivalSubtrees(root) {
  let count = 0;

  helper(root);

  return count;

  function helper(node) {
    if (!node) return false;

    if (!node.left && !node.right) {
      count++;
      return true;
    }

    let checkVal;
    let left = helper(node.left);
    let right = helper(node.right);

    if (node.left && node.right) {
      checkVal = node.left.val === node.val && node.right.val === node.val;
      if (left && right && checkVal) {
        count++;
        return true;
      }

    } else if (node.left) {
      checkVal = node.left.val === node.val;
      if (left && checkVal) {
        count++;
        return true;
      }
    } else {
      checkVal = node.right.val === node.val;
      if (right && checkVal) {
        count++;
        return true;
      }
    }
    
    return false;
  }
}
