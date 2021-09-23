function buildTree(preOrder, inOrder) {
  let indexMap = inOrder.reduce((acc, x, i) => {
    acc[x] = i;
    return acc;
  }, {});

  let preOrderIndex = 0;
  return helper(0, preOrder.length - 1);

  function helper(left, right) {
    if (left > right) return null;

    let current = preOrder[preOrderIndex++]
    let index = indexMap[current];

    let root = new TreeNode(current);

    root.left = helper(left, index - 1);
    root.right = helper(index + 1, right);

    return root;
  }
}
