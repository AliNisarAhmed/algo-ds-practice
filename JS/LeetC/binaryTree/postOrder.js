// Post order - Left > Right > Root
//

// Iterative
//
function postorderTraversal(root) {
  let res = [];
  let stack = [];

  let current = root;

  while (current !== null || stack.length > 0) {
    while (current) {
      stack.push(current);
      current = current.left;
    }

    current = stack.pop();

    if (current.right) {
      stack.push(current.right);
    } else {
      res.push(current.val);
    }
  }
  return res;
}

// Recursive
//

function postorderTraversal(root) {
  let res = [];

  helper(root, res);

  return res;

  function helper(node, res) {
    if (!node) return;

    if (node.left) {
      helper(node.left, res);
    }
    helper(node.right, res);
    res.push(node.val);
  }
}
