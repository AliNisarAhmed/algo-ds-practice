// Post order - Left > Right > Root
//


//  Iterative (with a recursive thinking) - with a stack and a linked list
function postorderTraversal(root) {
  let stack = [];
  let res = [];

  if (root == null) return res;

  stack.push(root);
  while (stack.length > 0) {
    let current = stack.pop();

    // Pushing to the "back" of the answer list, so that current.val is the last value in the list
    // better is to use a LinkedList to avoid O(n) insertion with unshift
    res.unshift(current.val);

    if (current.left !== null) {
      stack.push(current.left);
    }

    if (current.right !== null) {
      stack.push(current.right);
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

    helper(node.left, res);
    helper(node.right, res);
    res.push(node.val);
  }
}
