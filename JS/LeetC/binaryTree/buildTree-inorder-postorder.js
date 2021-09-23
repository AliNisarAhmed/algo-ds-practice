// inorder: left - root - right
// postorder: left - right - root

class TreeNode {
  constructor(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function buildTree(inOrder, postOrder) {
  let indexMap = inOrder.reduce((acc, x, i) => {
    acc[x] = i
    return acc;
  }, {});

  return helper(0, postOrder.length - 1);

  function helper(left, right) {
    if (left > right) return null;

    let current = postOrder.pop();
    let index = indexMap[current];

    let root = new TreeNode(current);


    root.right = helper(index + 1, right);
    root.left = helper(left, index - 1);

    return root;
  }
}
