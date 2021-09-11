// In Order Traversal
//
// Visit left > Root > Right

// If we have binary Search tree, in-order gets all the elements as sorted array
//


// Morris Traversal: https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
//

function inorderTraversal(root) {
  let res = [];

  let current = root; 
  let pre;

  while (current !== null) {
    if (!current.left) {
      res.push(current.val);
      current = current.right;
    } else {
      pre = current.left;
      while (pre.right) {
        pre = pre.right;
      }
      pre.right = current;
      let temp = current;
      current = current.left;
      temp.left = null
    }
  }

  return res;
}



// Iterative

// using a Stack
function inorderTraversal(root) {
  let stack = [];
  let res = [];

  let current = root;
  while (current !== null || stack.length > 0) {
    while (current !== null) {
      stack.push(current);
      current = current.left;
    }

    current = stack.pop();
    res.push(current.val);
    current = current.right;
  }

  return res;
}

function inorderTraversal(root) {
  let res = [];

  helper(root, res);

  return res;

  function helper(root, res) {
    if (!root) return res;

    helper(root.left, res);
    res.push(root.val);
    helper(root.right, res);
  }
}
